from account.entity.account import Account
from smart_content.entity.models import SmartContent
from smart_content.entity.smart_image import SmartImage
from smart_content.entity.smart_text import SmartText
from smart_content.repository.smart_content_repository import SmartContentRepository


class SmartContentRepositoryImpl(SmartContentRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, title, content_type, items, accountId):
        try:
            if accountId:
                account = Account.objects.get(id=accountId)
            else:
                account = None

            smart_content = SmartContent(
                title=title,
                content_type=content_type,
                account=account
            )
            smart_content.save()
        except Exception as e:
            print('Error saving SmartContent:', e)

        if items:
            for item in items:
                if item['type'] == 'text':
                    SmartText.objects.create(
                        content=smart_content,
                        text=item['content'],
                        sequence_number=item['sequence_number']
                    )
                elif item['type'] == 'image':
                    SmartImage.objects.create(
                        content=smart_content,
                        image_url=item['image_url'],
                        sequence_number=item['sequence_number']
                    )
        return smart_content

    def list(self):
        return SmartContent.objects.all().order_by('regDate')

    def listItems(self, contentId):
        try:
            smart_content = SmartContent.objects.get(id=contentId)

            texts = SmartText.objects.filter(content=smart_content).order_by('sequence_number')
            images = SmartImage.objects.filter(content=smart_content).order_by('sequence_number')

            items = []

            for text in texts:
                items.append({
                    'type': 'text',
                    'content': text.text,
                    'sequence_number': text.sequence_number
                })

            for image in images:
                items.append({
                    'type': 'image',
                    'image_url': image.image_url,
                    'sequence_number': image.sequence_number
                })

            items.sort(key=lambda x: x['sequence_number'])

            return items
        except SmartContent.DoesNotExist:
            raise Exception('SmartContent not found')