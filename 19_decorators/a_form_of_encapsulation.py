class Multiply:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def __call__(self):
        print(f"multiply {self.numbers}")
        self.checker(self.numbers)
        self.result = 1
        for num in self.numbers:
            self.result *= num
        print(self.result)
    
    @staticmethod
    def checker(numbers):
        for num in numbers:
            if type(num) != int:
                print("method")
                raise Exception("Accepts only integers.")
            
valid = Multiply([1,2,3])
invalid = Multiply([1,2,"three"])
valid()
valid.checker([1,2,3])