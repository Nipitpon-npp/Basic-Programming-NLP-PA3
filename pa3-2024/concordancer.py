import nltk
class Concordancer:

    left_context_length = 50
    right_context_length = 50

    def __init__(self):
        """Insert your code here"""
        self.tokens = []
        self.left_context_length
        self.right_context_length


    def read_tokens(self, file_name):
        """
        Insert your docstring here
        """
        with open(file_name, 'r', encoding= 'utf-8') as f:
            text = f.read()
            self.tokens = nltk.wordpunct_tokenize(text)


    def find_concordance(self, query, num_words):
        """
        Insert your docstring here
        """
        results = ''
        for i in range(len(self.tokens)):
            if self.tokens[i] == query:
                left_context = ' '.join(self.tokens[max(i - num_words, 0):i])
                if len(left_context) < self.left_context_length:
                    left_context = ' ' * (self.left_context_length - len(left_context)) + left_context
                elif len(left_context) > self.left_context_length:
                    left_context = left_context[-(self.left_context_length):]

                right_context = ' '.join(self.tokens[i + 1:i + 1 + num_words])
                if len(right_context) < self.right_context_length:
                    right_context = right_context + ' ' * (self.right_context_length - len(right_context))
                elif len(right_context) > self.right_context_length:
                    right_context = right_context[:self.right_context_length]

                context = f"{left_context} {query} {right_context}" +'\n'
                results += context

        if len(results) == 0:
            print('"Query not found..."')
        else:
            print(str(results))
    

    def find_concordance_ngram(self, ngram_query, num_words):
        """
        Insert your docstring here
        """
        results = ''
        ngram_length = len(ngram_query.split(" "))

        for i in range(len(self.tokens) - ngram_length + 1):
            if ' '.join(self.tokens[i:i + ngram_length]) == ngram_query:
                left_context = ' '.join(self.tokens[max(i - num_words, 0):i])
                if len(left_context) < self.left_context_length:
                    left_context = ' ' * (self.left_context_length - len(left_context)) + left_context
                elif len(left_context) > self.left_context_length:
                    left_context = left_context[-(self.left_context_length):]

                right_context = ' '.join(self.tokens[i + ngram_length:i + ngram_length + num_words])
                if len(right_context) < self.right_context_length:
                    right_context = right_context + ' ' * (self.right_context_length - len(right_context))
                elif len(right_context) > self.right_context_length:
                    right_context = right_context[:self.right_context_length]

                context = f"{left_context} {ngram_query} {right_context}" +'\n'
                results += context

        if len(results) == 0:
            print('"Query not found..."')
        else:
            print(str(results))


    def compute_bigram_stats(self, query, output_file_name):
        """
        Insert your docstring here
        """
        bigram_counts = {}
        punctuation = set([',', '.', '\'', '\"', '!', '?', '-', ':', ';', '/', '(',')','[',']','{','}','=','@','#','$','%','^','&','*','+','_','|'])
        total_bigrams = 0

        for i in range(len(self.tokens) - 1):
            bigram = (self.tokens[i], self.tokens[i + 1])
            if self.tokens[i] == query:
                if bigram in bigram_counts and bigram[1][0] not in punctuation :
                    bigram_counts[bigram] += 1
                elif bigram not in bigram_counts and bigram[1][0] not in punctuation:
                    bigram_counts[bigram] = 1
                total_bigrams += 1

        sorted_bigram_counts = sorted(bigram_counts.items(), key=lambda item: item[1], reverse=True)

        with open(output_file_name, 'w', encoding='utf-8') as f:
            for i, sorted_bigram in enumerate(sorted_bigram_counts):
                if i < len(sorted_bigram_counts) - 1:
                    f.write(f"{sorted_bigram[0][0]} {sorted_bigram[0][1]} {sorted_bigram[1]}\n")
                else:
                    f.write(f"{sorted_bigram[0][0]} {sorted_bigram[0][1]} {sorted_bigram[1]}")
                    