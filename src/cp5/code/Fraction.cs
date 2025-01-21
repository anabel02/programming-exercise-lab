public class Fraction
{
    // Propiedades para almacenar el numerador y denominador de la fracción.
    public int Numerator { get; private set; }
    public int Denominator { get; private set; }
    
    // Constructor que inicializa el numerador y denominador y simplifica la fracción.
    public Fraction(int numerator, int denominator)
    {
        if (denominator == 0)
            throw new DivideByZeroException("Denominator cannot be zero.");

        Numerator = numerator;
        Denominator = denominator;

        Simplify();
    }

    // Método para simplificar la fracción dividiendo numerador y denominador
    // por su Máximo Común Divisor (mcd).
    private void Simplify()
    {
        int gcd = Gcd(Numerator, Denominator);
        Numerator /= gcd;
        Denominator /= gcd;
    }

    public override string ToString()
    {
        return $"{Numerator}/{Denominator}";
    }

    // Método auxiliar para calcular el Máximo Común Divisor (mcd) de dos números
    // usando el algoritmo de Euclides.
    private static int Gcd(int a, int b)
    {
        return b == 0 ? a : Gcd(b, a % b);
    }

    // Método auxiliar para calcular el Mínimo Común Múltiplo (mcm) de dos números.
    private static int Lcm(int a, int b)
    {
        return a / Gcd(a, b) * b;
    }

    // Método auxiliar para obtener la fracción opuesta.
    private static Fraction Negate(Fraction a)
    {
        return new Fraction(-a.Numerator, a.Denominator);
    }

    // Método auxiliar para sumar dos fracciones.
    private static Fraction Add(Fraction a, Fraction b)
    {
        int denominator = Lcm(a.Denominator, b.Denominator);
        int numerator = denominator / a.Denominator * a.Numerator +
                        denominator / b.Denominator * b.Numerator;
        return new Fraction(numerator, denominator);
    }

    // Método auxiliar para obtener el recíproco de la fracción
    private static Fraction Reciprocal(Fraction a)
    {
        return new Fraction(a.Denominator, a.Numerator);
    }

    // Método auxiliar para multiplicar dos fracciones.
    private static Fraction Multiply(Fraction a, Fraction b)
    {
        return new Fraction(a.Numerator * b.Numerator, a.Denominator * b.Denominator);
    }

    // Operadores de positivo, negativo, suma, resta, multiplicación y división
    public static Fraction operator +(Fraction a)
    {
        return a;
    }

    public static Fraction operator -(Fraction a)
    {
        return Negate(a);
    }

    public static Fraction operator +(Fraction a, Fraction b)
    {
        return Add(a, b);
    }

    public static Fraction operator -(Fraction a, Fraction b)
    {
        return a + (-b);
    }

    public static Fraction operator *(Fraction a, Fraction b)
    {
        return Multiply(a, b);
    }

    public static Fraction operator /(Fraction a, Fraction b)
    {
        return a * Reciprocal(b);
    }
    
    // Conversión implícita de int a Fraction
    public static implicit operator Fraction(int number)
    {
        return new Fraction(number, 1);
    }

    // Método auxiliar para comparar dos fracciones devolviendo un entero.
    // -1 si `a < b`, 1 si `a > b` y 0 si son iguales.
    private static int Compare(Fraction a, Fraction b)
    {
        return (a.Numerator * b.Denominator).CompareTo(b.Numerator * a.Denominator);
    }

    // Operadores de comparación para fracciones
    public static bool operator ==(Fraction a, Fraction b)
    {
        return Compare(a, b) == 0;
    }

    public static bool operator !=(Fraction a, Fraction b)
    {
        return Compare(a, b) != 0;
    }

    public static bool operator <(Fraction a, Fraction b)
    {
        return Compare(a, b) < 0;
    }

    public static bool operator >(Fraction a, Fraction b)
    {
        return Compare(a, b) > 0;
    }

    public static bool operator <=(Fraction a, Fraction b)
    {
        return Compare(a, b) <= 0;
    }

    public static bool operator >=(Fraction a, Fraction b)
    {
        return Compare(a, b) >= 0;
    }
}
