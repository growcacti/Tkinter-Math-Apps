class MathOperations:
    def __init__(self):
        self.factorial_cache = {}
        
    def stirling_approximation(self,num):
        """
        Uses Stirling approximation to find the factorial of a number. Will NOT return the exact factorial, but an
        approximation of it
        :param num: Number to get factorial of
        :type num int
        :return: Factorial approximation of num
        :rtype: float
        """
        return sqrt(2 * pi * num) * ((num / e) ** num)


    # @memoize
    def factorial(self,num):
        """
        find the factorial of the given number
        :param num: Number
        :return: Factorial of num
        :rtype: int
        """
        cache = {}

        if num in cache:
            return cache[num]

        if num == 0:
            return 1

        else:
            x = num * factorial(num - 1)
            cache[num] = x
            return x
        # return 1 if num == 0 else num * factorial(num - 1)


    def factorial_digit_sum(self,num):
        """
        Finds the sum of the digits in the factorial of num

        An example:
        >>> factorial_digit_sum(10)
        27

        :param num: Number
        :type num int
        :return: sum of digits in the factorial of num
        :rtype: int
        """

        # sanity checks
        if num is None or not isinstance(num, (int, float)):
            raise ValueError(f"Expected number to be a number, instead got {num}")

        # convert to integer, in the case of floats
        num = int(num)

        # find the factorial of the number
        num_factorial = factorial(num)

        return sum(map(int, str(num_factorial)))


    def factorial_length(self,num):
        """
        Finds the length of the factorial of number num

        >>> factorial_length(5)
        3

        :param num:
        :type num int
        :return: Length of factorial i.e. number of digits in factorial
        :rtype: int
        """
        n_factorial = math_factorial(num)

        return len(str(n_factorial))


    def zeros(self,n: int) -> int:
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count


    def filter_me(self,num_list):
        evens = filter(lambda x: x % 2 == 0, num_list)
        return list(evens)


    def median(self,lst):
        """
        func to find median in a list
        """
        sort_list = sorted(lst)
        med = 0
        if len(sort_list) == 1:
            med = sort_list[0]
        elif len(sort_list) % 2 == 0:
            f_mid_index = len(sort_list) / 2
            s_mid_index = f_mid_index - 1
            med = (sort_list[f_mid_index] + sort_list[s_mid_index]) / 2.0
        elif len(sort_list) % 2 != 0:
            f_mid_index = len(sort_list) / 2
            med = sort_list[f_mid_index]
        return med

