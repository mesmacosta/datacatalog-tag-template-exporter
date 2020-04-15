import unittest
from unittest import mock

import datacatalog_tag_template_exporter
from datacatalog_tag_template_exporter import datacatalog_tag_template_exporter_cli


class TagManagerCLITest(unittest.TestCase):

    def test_parse_args_invalid_subcommand_should_raise_system_exit(self):
        self.assertRaises(
            SystemExit,
            datacatalog_tag_template_exporter_cli.DatacatalogTagTemplateExporterCLI._parse_args,
            ['invalid-subcommand'])

    def test_parse_args_create_tags_missing_mandatory_args_should_raise_system_exit(self):
        self.assertRaises(
            SystemExit,
            datacatalog_tag_template_exporter_cli.DatacatalogTagTemplateExporterCLI._parse_args,
            ['tag-templates', 'export'])

    def test_run_no_args_should_raise_attribute_error(self):
        self.assertRaises(
            AttributeError,
            datacatalog_tag_template_exporter_cli.DatacatalogTagTemplateExporterCLI.run, None)

    @mock.patch('datacatalog_tag_template_exporter.datacatalog_tag_template_exporter_cli.'
                'tag_template_datasource_exporter.'
                'TagTemplateDatasourceExporter')
    def test_run_export_tag_templates_should_call_correct_method(
        self, mock_tag_template_datasource_exporter):  # noqa: E125

        datacatalog_tag_template_exporter_cli.DatacatalogTagTemplateExporterCLI.run([
            'tag-templates', 'export', '--file-path', 'test.csv', '--project-ids',
            'my-project1,my-project2'
        ])

        tag_template_datasource_processor = mock_tag_template_datasource_exporter.return_value
        tag_template_datasource_processor.export_tag_templates.assert_called_once()
        tag_template_datasource_processor.export_tag_templates.assert_called_with(
            project_ids='my-project1,my-project2', file_path='test.csv')

    @mock.patch('datacatalog_tag_template_exporter.datacatalog_tag_template_exporter_cli.'
                'DatacatalogTagTemplateExporterCLI')
    def test_main_should_call_cli_run(self, mock_cli):
        datacatalog_tag_template_exporter.main()
        mock_cli.run.assert_called_once()
