class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(n):
            m = i+1
            if m%3==0 and m%5==0:
                answer.append("FizzBuzz")
            elif m%3==0:
                answer.append("Fizz")
            elif m%5==0:
                answer.append("Buzz")
            else:
                answer.append(str(m))
        return answer