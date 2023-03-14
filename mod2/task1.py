import os

class RSS:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    OUTPUT_FILE = os.path.join(BASE_DIR, 'output_file.txt')
    DIMENSION = ['B', 'KiB', 'MiB', 'GiB']

    @staticmethod
    def get_summary_rss(file_path: str) -> float:
        with open(file_path) as ps_output_file:
            columns_names = ps_output_file.readline()
            rss_column_number = columns_names.split().index('RSS')
            result_bytes = 0
            for i_line in ps_output_file.readlines():
                result_bytes += float(i_line.split()[rss_column_number])
            return result_bytes


    @staticmethod
    def rss_to_str(summary_rss: float) -> str:
        dimension_ind = 0
        while summary_rss // 1024 > 1:
            dimension_ind += 1
            summary_rss /= 1024
        return f'Summary rss: {summary_rss:.3f} {RSS.DIMENSION[dimension_ind]} '

if __name__ == '__main__':
    result = RSS.rss_to_str(RSS.get_summary_rss(RSS.OUTPUT_FILE))
    print(result)
