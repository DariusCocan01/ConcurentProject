class Combiner:
    def __init__(self, file1, file2, file3):
        self.file1 = file1
        self.file2 = file2
        self.file3 = file3

    def combine_files(self):
        with open('s_final.txt', 'w') as final_file:
            for filename in [self.file1, self.file2, self.file3]:
                with open(filename, 'r') as file:
                    final_file.write(file.read() + "\n\n")

combiner = Combiner('s1.txt', 's2.txt', 's3.txt')
combiner.combine_files()