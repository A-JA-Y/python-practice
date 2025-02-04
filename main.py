# Suggested code may be subject to a license. Learn more: ~LicenseLog:2624359296.
  # 1. perfect square 
def isPerfectSquare(num):
    """
    Checks if a number is a perfect square.
    
    Args:
      num: The number to check.
    
    Returns:
      True if the number is a perfect square, False otherwise.
    """
    if num < 0:
        return False
    if num == 0:
      return True
    x = int(num**0.5)
    return x * x == num
            
print(isPerfectSquare(1))

        