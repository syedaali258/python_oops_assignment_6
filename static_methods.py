class TempratureConverter:
    
    @staticmethod
    def celcius_to_fahrenheit(c):
        return(c * 9/5)  + 32
        

if __name__ == "__main__":
    print("Fahrenheit:", TempratureConverter.celcius_to_fahrenheit(0))
    print("Fahrenheit:", TempratureConverter.celcius_to_fahrenheit(100))