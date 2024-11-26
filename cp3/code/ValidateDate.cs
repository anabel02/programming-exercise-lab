public static class Program
{
    public static void Main()
    {
        Console.WriteLine("Introduce el día:");
        int day = int.Parse(Console.ReadLine() ?? string.Empty);
        Console.WriteLine("Introduce el mes:");
        int month = int.Parse(Console.ReadLine() ?? string.Empty);
        Console.WriteLine("Introduce el año:");
        int year = int.Parse(Console.ReadLine() ?? string.Empty);
    
        Console.WriteLine(
            ValidateDate(day, month, year)
                ? $"{day}/{month}/{year}" 
                : "No es fecha");
    }

    public static bool ValidateDate(int day, int month, int year)
    {
        return year > 0 &&
               month > 0 && month <= 12 &&
               day > 0 && day <= CalculateLastDayInMonth(month, year);
    }

    private static int CalculateLastDayInMonth(int month, int year)
    {
        switch (month)
        {
            // Los meses con 30 días
            case 4 or 6 or 9 or 11:
                return 30;
            // Febrero
            case 2:
                return IsLeapYear(year) ? 29 : 28;
            // Los meses con 31 días
            default:
                return 31;
        }
    }

    private static bool IsLeapYear(int year)
    {
        return year <= 1582
            ? year % 4 == 0
            : (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
    }
}