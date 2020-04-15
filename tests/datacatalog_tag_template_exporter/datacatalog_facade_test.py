import unittest
from unittest import mock

from google.api_core import exceptions

from datacatalog_tag_template_exporter import datacatalog_facade


class DataCatalogFacadeTest(unittest.TestCase):

    @mock.patch('datacatalog_tag_template_exporter.datacatalog_facade.'
                'datacatalog.DataCatalogClient')
    def setUp(self, mock_datacatalog_client):
        self.__datacatalog_facade = datacatalog_facade.DataCatalogFacade()
        # Shortcut for the object assigned to self.__datacatalog_facade.__datacatalog
        self.__datacatalog_client = mock_datacatalog_client.return_value

    def test_constructor_should_set_instance_attributes(self):
        self.assertIsNotNone(self.__datacatalog_facade.__dict__['_DataCatalogFacade__datacatalog'])

    def test_get_tag_template_should_call_client_library_method(self):
        self.__datacatalog_facade.get_tag_template(None)

        datacatalog = self.__datacatalog_client
        datacatalog.get_tag_template.assert_called_once()

    def test_search_tag_templates_should_return_values(self):
        result_iterator = MockedObject()

        entry = MockedObject()
        entry.name = 'template_1'

        entry_2 = MockedObject()
        entry_2.name = 'template_2'

        expected_return_value = [entry, entry_2]

        # simulates two pages
        result_iterator.pages = [[entry], [entry_2]]

        datacatalog = self.__datacatalog_client
        datacatalog.search_catalog.return_value = result_iterator

        return_value = self.__datacatalog_facade.search_tag_templates('my-project1,my-project2')

        self.assertEqual(1, datacatalog.search_catalog.call_count)
        self.assertEqual(expected_return_value, return_value)

    def test_get_tag_templates_from_search_results_should_return_values(self):
        entry = MockedObject()
        entry.name = 'asset_1'
        entry.relative_resource_name = 'asset_1_resource_name'

        entry_2 = MockedObject()
        entry_2.name = 'asset_2'
        entry_2.relative_resource_name = 'asset_2_resource_name'

        search_results = [entry, entry_2]

        datacatalog = self.__datacatalog_client
        datacatalog.get_tag_template.return_value = {}

        return_value = self.__datacatalog_facade.get_tag_templates_from_search_results(
            search_results)

        self.assertEqual(2, datacatalog.get_tag_template.call_count)
        self.assertEqual([{}, {}], return_value)

    def test_get_tag_templates_err_from_search_results_should_return_values(self):
        entry = MockedObject()
        entry.name = 'asset_1'
        entry.relative_resource_name = 'asset_1_resource_name'

        entry_2 = MockedObject()
        entry_2.name = 'asset_2'
        entry_2.relative_resource_name = 'asset_2_resource_name'

        search_results = [entry, entry_2]

        datacatalog = self.__datacatalog_client
        datacatalog.get_tag_template.side_effect = [
            {}, exceptions.GoogleAPICallError('Permission denied')
        ]

        return_value = self.__datacatalog_facade.get_tag_templates_from_search_results(
            search_results)

        self.assertEqual(2, datacatalog.get_tag_template.call_count)
        self.assertEqual([{}], return_value)


class MockedObject(object):

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, key):
        return self.__dict__[key]
