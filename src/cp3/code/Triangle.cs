public static class Program
{
    public static void Main()
    {
        Console.WriteLine("Introduce el primer lado:");
        int side1 = int.Parse(Console.ReadLine() ?? string.Empty);
        Console.WriteLine("Introduce el segundo lado:");
        int side2 = int.Parse(Console.ReadLine() ?? string.Empty);
        Console.WriteLine("Introduce el tercer lado:");
        int side3 = int.Parse(Console.ReadLine() ?? string.Empty);
    
        TypeOfTriangle typeOfTriangle = GetTypeOfTriangle(side1, side2, side3);
        int response = (int)typeOfTriangle;
    
        Console.WriteLine($"El tipo de triángulo es: {response}");
    }

    private enum TypeOfTriangle
    {
        NotATriangle = 0,
        Scalene = 1,
        Isosceles = 2,
        Equilateral = 3
    }

    private static TypeOfTriangle GetTypeOfTriangle(int side1, int side2, int side3)
    {
        if (side1 + side2 <= side3 || side1 + side3 <= side2 || side2 + side3 <= side1)
            return TypeOfTriangle.NotATriangle;

        if (side1 == side2 && side2 == side3)
            return TypeOfTriangle.Equilateral;

        if (side1 == side2 || side2 == side3 || side1 == side3)
            return TypeOfTriangle.Isosceles;

        return TypeOfTriangle.Scalene;
    }
}