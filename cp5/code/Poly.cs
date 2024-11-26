using System.Text;

public class Poly
{
    // Almacena los coeficientes del polinomio.
    // Asegura que el arreglo solo contenga coeficientes significativos.
    private int[] _coefficients;

    /// Obtiene el grado del polinomio.
    public int Degree => _coefficients.Length - 1;

    /// Índice para acceder a los coeficientes del polinomio.
    public int this[int coeff] => coeff > Degree ? 0 : _coefficients[coeff];

    public Poly(int[] elements)
    {
        if (elements == null)
            throw new ArgumentNullException(nameof(elements));

        _coefficients = RemoveTrailingZeros(elements);
    }

    /// Elimina los ceros redundantes al final de los coeficientes de un polinomio.
    private static int[] RemoveTrailingZeros(int[] coefficients)
    {
        // Encuentra el índice del último elemento no cero en el arreglo.
        int lastNonZeroIndex = FindLastNonZeroIndex(coefficients);

        // Si todos los elementos son 0, considera el grado como 0.
        int degree = lastNonZeroIndex == -1 ? 0 : lastNonZeroIndex;

        // Crea un nuevo arreglo con los elementos significativos.
        int[] simplifiedCoefficients = new int[degree + 1];
        Array.Copy(coefficients, simplifiedCoefficients, degree + 1);

        return simplifiedCoefficients;
    }
    
    /// Devuelve el índice del último elemento distinto de 0.
    /// Devuelve -1 si todos son 0
    private static int FindLastNonZeroIndex(int[] array)
    {
        // Recorre el arreglo de atrás hacia adelante 
        // para encontrar el último elemento no cero.
        for (int i = array.Length - 1; i >= 0; i--)
        {
            if (array[i] != 0)
            {
                return i;
            }
        }

        // Si todos los elementos son 0, devuelve -1.
        return -1;
    }

    /// Convierte el polinomio a una representación en cadena legible por humanos, 
    /// como "3x^2 - x + 1".
    public override string ToString()
    {
        var sb = new StringBuilder();
        for (int i = Degree; i >= 0; i--)
        {
            int coefficient = this[i];
            if (coefficient == 0) continue; // Omitir términos con coeficiente 0
    
            // Manejar el signo del término
            if (sb.Length > 0) // Si ya se añadió algún coeficiente
                sb.Append(coefficient > 0 ? " + " : " - ");
            else if (coefficient < 0)
                sb.Append('-');
    
            int absValue = Math.Abs(coefficient);
    
            // Construir el término según su exponente
            if (i == 0)
                sb.Append(absValue);
            else if (absValue == 1)
                sb.Append(i == 1 ? "x" : $"x^{i}"); // Omitir el coeficiente "1"
            else
                sb.Append(i == 1 ? $"{absValue}x" : $"{absValue}x^{i}");
        }
    
        // Devolver "0" si todos los coeficientes son 0
        return sb.Length > 0 ? sb.ToString() : "0";
    }
    
    /// Suma dos polinomios y devuelve un nuevo polinomio que representa el resultado.
    private static Poly Add(Poly a, Poly b) => AddOrSubtract(a, b, false);

    /// Resta un polinomio de otro y devuelve un nuevo polinomio que representa el resultado.
    private static Poly Subtract(Poly a, Poly b) => AddOrSubtract(a, b, true);
    
    // Método auxiliar para sumar o restar dos polinomios
    private static Poly AddOrSubtract(Poly a, Poly b, bool isSubtraction)
    {
        int maxDegree = Math.Max(a.Degree, b.Degree);
        int[] result = new int[maxDegree + 1];

        for (int i = 0; i < result.Length; i++)
        {
            if (isSubtraction)
                result[i] = a[i] - b[i];
            else
                result[i] = a[i] + b[i];
        }

        return new Poly(result);
    }

    /// Multiplica dos polinomios y devuelve el polinomio resultante.
    private static Poly Multiply(Poly a, Poly b)
    {
        int[] result = new int[a.Degree + b.Degree + 1];

        for (int i = 0; i <= a.Degree; i++)
        {
            for (int j = 0; j <= b.Degree; j++)
            {
                result[i + j] += a[i] * b[j];
            }
        }

        return new Poly(result);
    }

    /// Divide un polinomio por otro y devuelve el cociente y el residuo.
    private static (Poly Quotient, Poly Remainder) Divide(Poly dividend, Poly divisor)
    {
        throw new NotImplementedException();
    }

    /// Calcula la derivada del polinomio dado.
     private static Poly Derive(Poly poly)
     {
         if (poly.Degree == 0)
             return 0;

         int[] result = new int[poly.Degree];

         for (int i = 1; i <= poly.Degree; i++)
         {
             result[i - 1] = poly[i] * i;
         }

         return new Poly(result);
     }

    // Sobrecarga de operadores aritméticos
    public static Poly operator +(Poly a, Poly b) => Add(a, b);
    public static Poly operator -(Poly a, Poly b) => Subtract(a, b);
    public static Poly operator *(Poly a, Poly b) => Multiply(a, b);
    public static Poly operator /(Poly a, Poly b) => Divide(a, b).Quotient;
    public static Poly operator %(Poly a, Poly b) => Divide(a, b).Remainder;
    
    /// Devuelve la derivada del polinomio actual.
    public Poly Derivative() => Derive(this);
    
    /// Evalúa el polinomio en un valor específico de x.
    public int Evaluate(int x)
    {
        int res = 0;
        int acc = 1;

        // En lugar de usar Math.Pow que calcularía x^i en cada iteración, se utiliza
        // la variable 'acc' para almacenar el valor de x elevado a la potencia actual, 
        // multiplicándolo por x en cada paso.
        for (int i = 0; i <= Degree; i++)
        {
            res += this[i] * acc;
            acc *= x;
        }

        return res;
    }

    /// Convierte implícitamente un número entero a un polinomio.
    public static implicit operator Poly(int number) => new Poly([number]);

    /// Compara dos polinomios y devuelve un valor entero que indica su orden relativo.
    /// <returns>
    /// Devuelve:
    /// -1 si <paramref name="a"/> es menor que <paramref name="b"/>.
    ///  1 si <paramref name="a"/> es mayor que <paramref name="b"/>.
    ///  0 si <paramref name="a"/> y <paramref name="b"/> son iguales.
    /// </returns>
    private static int Compare(Poly a, Poly b)
    {
        throw new NotImplementedException();
    }

    // Sobrecarga de operadores de comparación
    public static bool operator ==(Poly a, Poly b) => Compare(a, b) == 0;
    public static bool operator !=(Poly a, Poly b) => Compare(a, b) != 0;
    public static bool operator <(Poly a, Poly b) => Compare(a, b) < 0;
    public static bool operator >(Poly a, Poly b) => Compare(a, b) > 0;
    public static bool operator <=(Poly a, Poly b) => Compare(a, b) <= 0;
    public static bool operator >=(Poly a, Poly b) => Compare(a, b) >= 0;
}