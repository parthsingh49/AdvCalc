import math
import cmath
import numpy as np

class AdvancedCalculator:
    def __init__(self):
        """Initialize the advanced calculator with memory and last result."""
        self.memory = 0
        self.last_result = None

    def perform_basic_operation(self, operation, x, y=None):
        """Execute basic arithmetic operations."""
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

    def calculate_trigonometric(self, function, x, mode='degrees'):
        """Calculate trigonometric functions with degree/radian support."""
        try:
            if mode == 'degrees':
                x = math.radians(x)
            if function == 'sin':
                return math.sin(x)
            elif function == 'cos':
                return math.cos(x)
            elif function == 'tan':
                return math.tan(x)
            elif function in ['arcsin', 'arccos', 'arctan']:
                angle_func = getattr(math, function)
                return math.degrees(angle_func(x)) if mode == 'degrees' else angle_func(x)
        except Exception as e:
            return f"Error: {str(e)}"

    def exponential_and_logarithmic(self, function, x):
        """Perform exponential and logarithmic calculations."""
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

    def complex_operations(self, operation, real, imag):
        """Handle operations involving complex numbers."""
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

    def statistical_calculations(self, function, numbers):
        """Execute statistical functions on a list of numbers."""
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

    def memory_management(self, operation, value=None):
        """Manage memory operations."""
        if operation == 'store':
            self.memory = value
        elif operation == 'recall':
            return self.memory
        elif operation == 'clear':
            self.memory = 0
        return self.memory

def main():
    calculator = AdvancedCalculator()
    print("Welcome to the Advanced Calculator!")
    print("Available Operations:")
    print("1. Basic Operations (+, -, *, /, %, **)")
    print("2. Trigonometric Functions")
    print("3. Exponential and Logarithmic Functions")
    print("4. Complex Number Operations")
    print("5. Statistical Functions")
    print("6. Memory Operations")
    
    while True:
        try:
            category = input("\nSelect category (or type 'exit' to quit): ").lower()
            if category == 'exit':
                break
            
            if category == '1':
                op = input("Choose an operation (+, -, *, /, %, **): ")
                x = float(input("Enter first number: "))
                y = float(input("Enter second number (if applicable): ")) if op != '%' else None
                result = calculator.perform_basic_operation(op, x, y)
                
            elif category == '2':
                func = input("Enter trigonometric function (sin, cos, tan, arcsin, arccos, arctan): ")
                x = float(input("Enter value: "))
                mode = input("Enter mode (degrees/radians; default is degrees): ").lower() or 'degrees'
                result = calculator.calculate_trigonometric(func, x, mode)

            elif category == '3':
                func = input("Enter function (exp, log, log10, sqrt, power): ")
                x = float(input("Enter value: "))
                result = calculator.exponential_and_logarithmic(func, x)

            elif category == '4':
                func = input("Enter complex operation (magnitude, phase, conjugate): ")
                real = float(input("Enter real part: "))
                imag = float(input("Enter imaginary part: "))
                result = calculator.complex_operations(func, real, imag)

            elif category == '5':
                func = input("Enter statistical function (mean, median, std, variance): ")
                numbers = list(map(float, input("Enter numbers (space-separated): ").split()))
                result = calculator.statistical_calculations(func, numbers)

            elif category == '6':
                func = input("Enter memory operation (store, recall, clear): ")
                if func == 'store':
                    value = float(input("Enter value to store in memory: "))
                    calculator.memory_management(func, value)
                    result = "Value stored."
                else:
                    result = calculator.memory_management(func)

            else:
                result = "Invalid selection. Please try again."

            print(f"Result: {result}")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()