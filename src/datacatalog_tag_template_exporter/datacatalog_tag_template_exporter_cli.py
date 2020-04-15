import argparse
import logging
import sys

from datacatalog_tag_template_exporter import tag_template_datasource_exporter


class DatacatalogTagTemplateExporterCLI:

    @classmethod
    def run(cls, argv):
        cls.__setup_logging()

        args = cls._parse_args(argv)
        args.func(args)

    @classmethod
    def __setup_logging(cls):
        logging.basicConfig(level=logging.INFO)

    @classmethod
    def _parse_args(cls, argv):
        parser = argparse.ArgumentParser(description=__doc__,
                                         formatter_class=argparse.RawDescriptionHelpFormatter)

        subparsers = parser.add_subparsers()

        cls.add_tag_templates_cmd(subparsers)

        return parser.parse_args(argv)

    @classmethod
    def add_tag_templates_cmd(cls, subparsers):
        tag_templates_parser = subparsers.add_parser("tag-templates",
                                                     help="Tag Templates commands")

        tag_templates_subparsers = tag_templates_parser.add_subparsers()

        cls.add_export_tag_templates_cmd(tag_templates_subparsers)

    @classmethod
    def add_export_tag_templates_cmd(cls, subparsers):
        export_tag_templates_parser = subparsers.add_parser('export',
                                                            help='Export Tag Templates to CSV')
        export_tag_templates_parser.add_argument('--file-path',
                                                 help='File path where file will be exported')
        export_tag_templates_parser.add_argument('--project-ids',
                                                 help='Project ids to narrow down Templates list,'
                                                 'split by comma',
                                                 required=True)
        export_tag_templates_parser.set_defaults(func=cls.__export_tag_templates)

    @classmethod
    def __export_tag_templates(cls, args):
        tag_template_datasource_exporter.TagTemplateDatasourceExporter().export_tag_templates(
            project_ids=args.project_ids, file_path=args.file_path)


def main():
    argv = sys.argv
    DatacatalogTagTemplateExporterCLI.run(argv[1:] if len(argv) > 0 else argv)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
