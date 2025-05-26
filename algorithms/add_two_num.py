class Solution(object):
    def addTwoNumbers(self, l_num_1, l_num_2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Reversing the sequence of numbers
        self.l1 = l_num_1
        self.l2 = l_num_2

        # Join num in a string and convert in an integer
        first = int(''.join(map(str, self.l1)))
        print(first)
        second = int(''.join(map(str, self.l2)))
        print(second)

        # Add numbers and convert in string
        final_count= first+second
        print(final_count)
        final_count_str = str(final_count)
        # Iterate over digits and append to a list as integers
        digit_list = [int(char) for char in final_count_str][::-1]
        
        
        return digit_list

l_num_1 = [2, 4, 3]
l_num_2 = [5, 6, 4]
solution = Solution()
result = solution.addTwoNumbers(l_num_1, l_num_2)
print(result)