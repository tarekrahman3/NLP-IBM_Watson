import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions

"""Go to the IBM Cloud Dashboard page.
Either click an existing Watson service instance in your resource list or click Create resource > AI and create a service instance.
Click on the Manage item in the left nav bar of your service instance."""

authenticator = IAMAuthenticator('api')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-08-01',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/{value-see docstring}')

response = natural_language_understanding.analyze(
    url='https://www.collinsdictionary.com/dictionary/english/story',
    features=Features(
        entities=EntitiesOptions(emotion=True, sentiment=True, limit=2),
        keywords=KeywordsOptions(emotion=True, sentiment=True,
                                 limit=2))).get_result()

print(json.dumps(response, indent=2))
