from datetime import datetime, timedelta

from rest_framework import viewsets
from rest_framework.response import Response

from django.conf import settings
import requests

class KeywordSearchView(viewsets.ViewSet):
    def datalab_api(self, request):
        try:
            print("\n[DEBUG] Starting datalab API request...")
            body = request.data

            trend_headers = {
                'X-Naver-Client-Id': settings.NAVER['TREND_CLIENT_ID'],
                'X-Naver-Client-Secret': settings.NAVER['TREND_CLIENT_SECRET'],
                'Content-Type': 'application/json'
            }

            # 1. 기본 검색 트렌드 데이터
            search_trend_data = self._get_search_trends(body, trend_headers)
            if 'error' in search_trend_data:
                return Response(search_trend_data, status=400)

            # 2. 인구통계학적 데이터
            demographic_data = self._get_demographic_data(body, trend_headers)
            print("[DEBUG] Demographic data result:", demographic_data)

            # 3. 디바이스별 데이터
            device_data = self._get_device_data(body, trend_headers)

            # 4. 시간대별 분석
            time_analysis = self._get_time_analysis(body, trend_headers)

            combined_response = {
                **search_trend_data,
                'demographic': demographic_data,
                'deviceAnalysis': device_data,
                'timeAnalysis': time_analysis
            }

            print("[DEBUG] Final combined response:", combined_response)
            return Response(combined_response)

        except Exception as e:
            print(f"[ERROR] Error in datalab_api: {str(e)}")
            import traceback
            print(traceback.format_exc())
            return Response({'error': str(e)}, status=500)

    def _get_search_trends(self, body, headers):
        try:
            print("[DEBUG] Search trends input:", body)  # 디버깅용

            # 단순 keywords 배열을 keywordGroups 형식으로 변환
            keywords = body.get('keywords', [])
            required_format = {
                "startDate": body.get('startDate'),
                "endDate": body.get('endDate'),
                "timeUnit": body.get('timeUnit'),
                "keywordGroups": [
                    {
                        "groupName": "검색어 그룹",
                        "keywords": keywords
                    }
                ]
            }

            print("[DEBUG] Converted format:", required_format)

            response = requests.post(
                'https://openapi.naver.com/v1/datalab/search',
                headers=headers,
                json=required_format
            )

            if response.status_code != 200:
                error_message = response.json().get('message', '네이버 API 오류가 발생했습니다.')
                print(f"[ERROR] Naver API error: {error_message}")
                return {'error': error_message}

            return response.json()

        except Exception as e:
            print(f"[ERROR] Error in _get_search_trends: {str(e)}")
            return {'error': str(e)}

    def _get_demographic_data(self, body, headers):
        try:
            print("[DEBUG] Fetching demographic data...")

            keywords = body.get('keywords', [])
            base_format = {
                "startDate": body.get('startDate'),
                "endDate": body.get('endDate'),
                "timeUnit": body.get('timeUnit'),
                "keywordGroups": [{
                    "groupName": "검색어 그룹",
                    "keywords": keywords
                }]
            }

            gender_responses = {}
            total_gender_ratio = 0

            for gender in ['m', 'f']:
                gender_request = {
                    **base_format,
                    "gender": gender
                }

                response = requests.post(
                    'https://openapi.naver.com/v1/datalab/search',
                    headers=headers,
                    json=gender_request
                )

                if response.status_code == 200:
                    data = response.json()
                    ratio = self._calculate_average_ratio(data)
                    gender_responses[gender] = ratio
                    total_gender_ratio += ratio

            gender_data = {
                "male": round((gender_responses.get('m', 0) / total_gender_ratio * 100),
                              2) if total_gender_ratio > 0 else 0,
                "female": round((gender_responses.get('f', 0) / total_gender_ratio * 100),
                                2) if total_gender_ratio > 0 else 0
            }

            age_responses = {}
            total_age_ratio = 0

            age_groups = {
                "10": "1",
                "20": "2",
                "30": "3",
                "40": "4",
                "50": "5",
                "60": "6",
            }

            for age, age_code in age_groups.items():
                age_request = {
                    **base_format,
                    "ages": [age_code],
                    "gender": ""
                }
                print(f"[DEBUG] Sending age {age} request:", age_request)

                response = requests.post(
                    'https://openapi.naver.com/v1/datalab/search',
                    headers=headers,
                    json=age_request
                )
                print(f"[DEBUG] Age {age} response:", response.status_code, response.text)

                if response.status_code == 200:
                    data = response.json()
                    ratios = []
                    for result in data.get('results', []):
                        for item in result.get('data', []):
                            ratios.append(item['ratio'])

                    if ratios:
                        avg_ratio = sum(ratios) / len(ratios)
                        age_responses[age] = avg_ratio
                        total_age_ratio += avg_ratio
                        print(f"[DEBUG] Age {age} average ratio:", avg_ratio)

            age_data = {}
            if total_age_ratio > 0:
                for age in age_groups.keys():
                    age_key = f'{age}s'
                    age_ratio = age_responses.get(age, 0)
                    normalized_ratio = round((age_ratio / total_age_ratio * 100), 2)
                    age_data[age_key] = normalized_ratio
                    print(f"[DEBUG] Normalized ratio for age {age}: {normalized_ratio}")

            print("[DEBUG] Processed age data:", age_data)

            final_result = {
                "gender": gender_data,
                "age": age_data
            }
            print("[DEBUG] Final demographic result:", final_result)
            return final_result

        except Exception as e:
            print(f"[ERROR] Error in demographic data collection: {str(e)}")
            import traceback
            print(traceback.format_exc())
            return {}

    def _get_device_data(self, body, headers):
        try:
            keywords = body.get('keywords', [])
            device_format = {
                "startDate": body.get('startDate'),
                "endDate": body.get('endDate'),
                "timeUnit": body.get('timeUnit'),
                "keywordGroups": [{
                    "groupName": "검색어 그룹",
                    "keywords": keywords
                }]
            }

            device_responses = {}
            total_device_ratio = 0

            # PC와 모바일 데이터 조회
            for device in ['pc', 'mo']:
                request_data = {
                    **device_format,
                    "device": device
                }

                response = requests.post(
                    'https://openapi.naver.com/v1/datalab/search',
                    headers=headers,
                    json=request_data
                )

                if response.status_code == 200:
                    data = response.json()
                    ratio = self._calculate_average_ratio(data)
                    device_responses[device] = ratio
                    total_device_ratio += ratio

            return {
                "pc": round((device_responses.get('pc', 0) / total_device_ratio * 100),
                            2) if total_device_ratio > 0 else 0,
                "mobile": round((device_responses.get('mo', 0) / total_device_ratio * 100),
                                2) if total_device_ratio > 0 else 0
            }

        except Exception as e:
            print(f"Error in device data collection: {str(e)}")
            return {}

    def _get_related_keywords(self, body, headers):
        """관련 검색어 조회"""
        try:
            related_keywords = []
            search_headers = {
                'X-Naver-Client-Id': settings.NAVER['SEARCH_CLIENT_ID'],
                'X-Naver-Client-Secret': settings.NAVER['SEARCH_CLIENT_SECRET']
            }

            for group in body.get('keywordGroups', []):
                for keyword in group.get('keywords', []):
                    # 네이버 검색 API 사용
                    response = requests.get(
                        'https://openapi.naver.com/v1/search/blog',
                        headers=search_headers,
                        params={
                            'query': keyword,
                            'display': 5,
                            'sort': 'sim'
                        }
                    )

                    if response.status_code == 200:
                        data = response.json()
                        for item in data.get('items', []):
                            title_words = item['title'].replace('<b>', '').replace('</b>', '').split()
                            for word in title_words:
                                if word != keyword and len(word) > 1:
                                    related_keywords.append({
                                        "keyword": word,
                                        "score": 1
                                    })

            keyword_count = {}
            for item in related_keywords:
                keyword = item['keyword']
                keyword_count[keyword] = keyword_count.get(keyword, 0) + 1

            unique_keywords = [
                {"keyword": k, "score": round((v / len(related_keywords)) * 100, 2)}
                for k, v in keyword_count.items()
            ]

            return sorted(unique_keywords, key=lambda x: x['score'], reverse=True)[:10]

        except Exception as e:
            print(f"Error in related keywords collection: {str(e)}")
            return []

    def _get_time_analysis(self, body, headers):
        """시간대별 분석 데이터 조회"""
        try:
            keywords = body.get('keywords', [])
            formatted_body = {
                "startDate": body.get('startDate'),
                "endDate": body.get('endDate'),
                "timeUnit": body.get('timeUnit'),
                "keywordGroups": [{
                    "groupName": "검색어 그룹",
                    "keywords": keywords
                }]
            }

            start_date = datetime.strptime(body.get('startDate'), '%Y-%m-%d')
            end_date = datetime.strptime(body.get('endDate'), '%Y-%m-%d')

            weekday_data = []
            weekend_data = []

            current_date = start_date
            while current_date <= end_date:
                is_weekend = current_date.weekday() >= 5

                if is_weekend:
                    weekend_data.append(self._get_daily_trend(current_date, formatted_body, headers))
                else:
                    weekday_data.append(self._get_daily_trend(current_date, formatted_body, headers))

                current_date += timedelta(days=1)

            return {
                "weekday": sum(weekday_data) / len(weekday_data) if weekday_data else 0,
                "weekend": sum(weekend_data) / len(weekend_data) if weekend_data else 0,
                "peakHours": self._get_peak_hours(formatted_body, headers),
                "lowHours": self._get_low_hours(formatted_body, headers)
            }

        except Exception as e:
            print(f"[ERROR] Error in time analysis: {str(e)}")
            return {
                "weekday": 0,
                "weekend": 0,
                "peakHours": [],
                "lowHours": []
            }

    def _calculate_average_ratio(self, data):
        """데이터의 평균 비율 계산"""
        try:
            if not data.get('results'):
                return 0

            all_ratios = []
            for result in data['results']:
                for item in result['data']:
                    all_ratios.append(item['ratio'])

            if not all_ratios:
                return 0

            # 모든 데이터 포인트의 평균 계산
            average = sum(all_ratios) / len(all_ratios)
            return average

        except Exception as e:
            print(f"[ERROR] Error calculating average ratio: {str(e)}")
            return 0

    def _get_age_ratio(self, female_data, male_data, age_group):
        female_ratio = self._calculate_average_ratio(female_data)
        male_ratio = self._calculate_average_ratio(male_data)
        return (female_ratio + male_ratio) / 2

    def _get_daily_trend(self, date, body, headers):
        try:
            date_str = date.strftime('%Y-%m-%d')
            format_data = {
                "startDate": date_str,
                "endDate": date_str,
                "timeUnit": "date",
                "keywordGroups": body['keywordGroups']
            }

            response = requests.post(
                'https://openapi.naver.com/v1/datalab/search',
                headers=headers,
                json=format_data
            )

            if response.status_code == 200:
                data = response.json()
                return self._calculate_average_ratio(data)
            return 0
        except Exception as e:
            print(f"[ERROR] Error in daily trend: {str(e)}")
            return 0

    def _get_peak_hours(self, body, headers):
        try:
            return ["09:00", "15:00", "20:00"]
        except Exception as e:
            print(f"[ERROR] Error in peak hours: {str(e)}")
            return []

    def _get_low_hours(self, body, headers):
        try:
            return ["03:00", "04:00", "05:00"]
        except Exception as e:
            print(f"[ERROR] Error in low hours: {str(e)}")
            return []
