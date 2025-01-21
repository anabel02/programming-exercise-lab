using System.Text;

public class BigInt
{
    // Almacena el número como una cadena para manejar números grandes
    private readonly string _value;

    // Propiedad para obtener la cantidad de dígitos del número almacenado
    private int DigitsCount => _value.Length;

    // Indexador que permite acceder a cada dígito como un entero.
    // Convierte el carácter en la posición `index` a su valor numérico (de '0' a '9').
    // Investiga sobre el código ASCII
    private int this[int index] => _value[index] - '0';

    // Constructor que recibe un número en forma de cadena de caracteres
    public BigInt(string value)
    {
        if (string.IsNullOrEmpty(value) || !IsValidNumber(value))
            throw new ArgumentException("El valor debe ser un número válido.");

        _value = RemoveLeadingZeros(value);
    }

    private static bool IsValidNumber(string value)
    {
        for (var i = 0; i < value.Length; i++)
        {
            if (!char.IsDigit(value[i]))
                return false;
        }

        return true;
    }

    private string RemoveLeadingZeros(string value)
    {
        // Elimina los ceros iniciales de la cadena
        value = value.TrimStart('0');

        // Si después de eliminar ceros iniciales la cadena queda vacía, asigna "0"
        return value == string.Empty ? "0" : value;
    }

    // Método para convertir el BigInt en una cadena de texto
    public override string ToString() => _value;

    // Sobrecarga de conversión implícita que permite convertir un int a BigInt
    public static implicit operator BigInt(int number) => new BigInt(number.ToString());

    // Operadores de suma, resta, multiplicación, división y módulo para BigInt
    public static BigInt operator +(BigInt a, BigInt b) => Add(a, b);
    public static BigInt operator -(BigInt a, BigInt b) => Subtract(a, b);
    public static BigInt operator *(BigInt a, BigInt b) => Multiply(a, b);
    public static BigInt operator /(BigInt a, BigInt b) => Divide(a, b).Quotient;
    public static BigInt operator %(BigInt a, BigInt b) => Divide(a, b).Remainder;

    // Operadores de comparación entre BigInt
    public static bool operator ==(BigInt a, BigInt b) => Compare(a, b) == 0;
    public static bool operator !=(BigInt a, BigInt b) => Compare(a, b) != 0;
    public static bool operator <(BigInt a, BigInt b) => Compare(a, b) < 0;
    public static bool operator >(BigInt a, BigInt b) => Compare(a, b) > 0;
    public static bool operator <=(BigInt a, BigInt b) => Compare(a, b) <= 0;
    public static bool operator >=(BigInt a, BigInt b) => Compare(a, b) >= 0;
    
    private static BigInt Add(BigInt a, BigInt b)
    {
        StringBuilder result = new();
        int carry = 0; // Variable para el acarreo
        int maxLength = Math.Max(a.DigitsCount, b.DigitsCount);

        // Sumar cada dígito empezando desde el menos significativo
        for (int i = 0; i < maxLength || carry > 0; i++)
        {
            int digitA = i < a.DigitsCount ? a[a.DigitsCount - 1 - i] : 0;
            int digitB = i < b.DigitsCount ? b[b.DigitsCount - 1 - i] : 0;
            int sum = digitA + digitB + carry;

            result.Insert(0, sum % 10); // Agrega el dígito al resultado
            carry = sum / 10; // Calcula el acarreo
        }

        return new BigInt(result.ToString());
    }

    private static BigInt Subtract(BigInt a, BigInt b)
    {
        throw new NotImplementedException("Debes implementar este método");
    }

    private static BigInt Multiply(BigInt a, BigInt b)
    {
        throw new NotImplementedException("Debes implementar este método");
    }

    // Método para dividir dos BigInt y retornar el cociente y el resto
    private static (BigInt Quotient, BigInt Remainder) Divide(BigInt a, BigInt b)
    {
        throw new NotImplementedException("Debes implementar este método");
    }

    public static BigInt Pow(BigInt a, BigInt b)
    {
        throw new NotImplementedException("Debes implementar este método");
    }

    // Método auxiliar para comparar dos BigInt devolviendo un entero.
    // -1 si `a < b`, 1 si `a > b` y 0 si son iguales.
    private static int Compare(BigInt a, BigInt b)
    {
        throw new NotImplementedException("Debes implementar este método");
    }
}