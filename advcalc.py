import math
import cmath
import numpy as np

class AIAdvancedCalculator:
    def __init__(self):
        """
        Initialize the AI-powered advanced calculator with various mathematical function categories.
        """
        self.memory = 0
        self.last_result = None

    def basic_operations(self, operation, x, y=None):
        """
        Perform basic arithmetic operations.
        
        :param operation: String indicating the operation (+, -, *, /, %, **)
        :param x: First number
        :param y: Second number (optional for some operations)
        :return: Result of the operation
        """
        try:
            if operation == '+':
                return x + y
            elif operation == '-':
                return x - y
            elif operation == '*':
                return x * y
            elif operation == '/':
                if y == 0:
                    return "Error: Division by zero"
                return x / y
            elif operation == '%':
                return x % y
            elif operation == '**':
                return x ** y
        except Exception as e:
            return f"Error: {str(e)}"

    def trigonometric_functions(self, function, x, mode='degrees'):
        """
        Perform trigonometric functions with degree/radian support.
        
        :param function: Trigonometric function (sin, cos, tan, etc.)
        :param x: Input value
        :param mode: 'degrees' or 'radians'
        :return: Result of the trigonometric function
        """
        try:
            # Convert to radians if input is in degrees
            if mode == 'degrees':
                x = math.radians(x)
            
            if function == 'sin':
                return math.sin(x)
            elif function == 'cos':
                return math.cos(x)
            elif function == 'tan':
                return math.tan(x)
            elif function == 'arcsin':
                return math.degrees(math.asin(x)) if mode == 'degrees' else math.asin(x)
            elif function == 'arccos':
                return math.degrees(math.acos(x)) if mode == 'degrees' else math.acos(x)
            elif function == 'arctan':
                return math.degrees(math.atan(x)) if mode == 'degrees' else math.atan(x)
        except Exception as e:
            return f"Error: {str(e)}"

    def exponential_and_logarithmic(self, function, x):
        """
        Perform exponential and logarithmic functions.
        
        :param function: Exponential/logarithmic function
        :param x: Input value
        :return: Result of the function
        """
        try:
            if function == 'exp':
                return math.exp(x)
            elif function == 'log':
                return math.log(x)
            elif function == 'log10':
                return math.log10(x)
            elif function == 'sqrt':
                return math.sqrt(x)
            elif function == 'power':
                return x ** 2
        except Exception as e:
            return f"Error: {str(e)}"

    def complex_numbers(self, operation, real, imag):
        """
        Perform operations with complex numbers.
        
        :param operation: Complex number operation
        :param real: Real part
        :param imag: Imaginary part
        :return: Result of the complex number operation
        """
        try:
            z = complex(real, imag)
            
            if operation == 'magnitude':
                return abs(z)
            elif operation == 'phase':
                return cmath.phase(z)
            elif operation == 'conjugate':
                return z.conjugate()
        except Exception as e:
            return f"Error: {str(e)}"

    def statistical_functions(self, function, numbers):
        """
        Perform statistical calculations.
        
        :param function: Statistical function
        :param numbers: List of numbers
        :return: Result of the statistical calculation
        """
        try:
            if function == 'mean':
                return np.mean(numbers)
            elif function == 'median':
                return np.median(numbers)
            elif function == 'std':
                return np.std(numbers)
            elif function == 'variance':
                return np.var(numbers)
        except Exception as e:
            return f"Error: {str(e)}"

    def memory_operations(self, operation, value=None):
        """
        Perform memory operations.
        
        :param operation: Memory operation
        :param value: Optional value for memory operations
        :return: Current memory value
        """
        if operation == 'store':
            self.memory = value
        elif operation == 'recall':
            return self.memory
        elif operation == 'clear':
            self.memory = 0
        return self.memory

def main():
    calculator = AIAdvancedCalculator()
    
    print("Welcome to AI-Powered Advanced Calculator!")
    print("Available Function Categories:")
    print("1. Basic Operations (+, -, *, /, %, **)")
    print("2. Trigonometric Functions")
    print("3. Exponential and Logarithmic Functions")
    print("4. Complex Number Operations")
    print("5. Statistical Functions")
    print("6. Memory Operations")
    
    while True:
        try:
            category = input("\nSelect category (or 'quit' to exit): ").lower()
            
            if category == 'quit':
                break
            
            if category == '1':
                op = input("Enter operation (+, -, *, /, %, **): ")
                x = float(input("Enter first number: "))
                y = float(input("Enter second number (if applicable): ")) if op != '%' else None
                result = calculator.basic_operations(op, x, y)
                print(f"Result: {result}")
            
            elif category == '2':
                func = input("Enter trigonometric function (sin, cos, tan, arcsin, arccos, arctan): ")
                x = float(input("Enter value: "))
                mode = input("Enter mode (degrees/radians, default is degrees): ").lower() or 'degrees'
                result = calculator.trigonometric_functions(func, x, mode)
                print(f"Result: {result}")
            
            elif category == '3':
                func = input("Enter function (exp, log, log10, sqrt, power): ")
                x = float(input("Enter value: "))
                result = calculator.exponential_and_logarithmic(func, x)
                print(f"Result: {result}")
            
            elif category == '4':
                func = input("Enter complex operation (magnitude, phase, conjugate): ")
                real = float(input("Enter real part: "))
                imag = float(input("Enter imaginary part: "))
                result = calculator.complex_numbers(func, real, imag)
                print(f"Result: {result}")
            
            elif category == '5':
                func = input("Enter statistical function (mean, median, std, variance): ")
                numbers = list(map(float, input("Enter numbers (space-separated): ").split()))
                result = calculator.statistical_functions(func, numbers)
                print(f"Result: {result}")
            
            elif category == '6':
                func = input("Enter memory operation (store, recall, clear): ")
                if func == 'store':
                    value = float(input("Enter value to store: "))
                    calculator.memory_operations(func, value)
                else:
                    result = calculator.memory_operations(func)
                    print(f"Memory value: {result}")
            
            else:
                print("Invalid category. Please try again.")
        
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()