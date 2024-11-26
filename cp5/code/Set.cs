public class Set
{
    // Usamos la clase List de C# para almacenar nuestros elementos
    private List<int> _elements;
    
    private int this[int value] => _elements[value];
    
    public int Cardinality => _elements.Count;

    // Propiedad privada que verifica si el conjunto está vacío
    private bool IsEmpty => Cardinality == 0;

    // Constructor que crea un conjunto vacío
    public Set()
    {
        _elements = new List<int>();
    }

    // Constructor que crea un conjunto a partir de una lista de elementos
    public Set(List<int> elements)
    {
        _elements = elements;
    }
    
    public bool Contains(int element)
    {
        return _elements.Contains(element);
    }
    
    public void Add(int element)
    {
        // Si ya estaba entre los elementos lo ignoramos, para evitar duplicados
        if (!Contains(element))
        {
            _elements.Add(element);
        }
    }

    public bool Remove(int element)
    {
        return _elements.Remove(element);
    }

    public void Clear()
    {
        _elements.Clear();
    }

    public static Set Intersection(Set a, Set b)
    {
        Set result = new Set();

        for (int i = 0; i < a.Cardinality; i++)
        {
            int element = a[i];
            if (b.Contains(element))
            {
                result.Add(element);
            }
        }

        return result;
    }

    public static Set Union(Set a, Set b)
    {
        Set result = new Set();

        for (int i = 0; i < a.Cardinality; i++)
        {
            result.Add(a[i]);
        }

        for (int i = 0; i < b.Cardinality; i++)
        {
            result.Add(b[i]);
        }

        return result;
    }

    public static Set Difference(Set a, Set b)
    {
        Set result = new Set();

        for (int i = 0; i < a.Cardinality; i++)
        {
            int element = a[i];
            if (!b.Contains(element))
            {
                result.Add(element);
            }
        }

        return result;
    }

    // Verifica si el conjunto `a` es un subconjunto de `b`.
    public static bool IsSubset(Set a, Set b) => Difference(a, b).IsEmpty;

    // Determina si dos conjuntos son iguales en contenido.
    private static bool Equals(Set a, Set b)
    {
        return IsSubset(a, b) && IsSubset(b, a);
    }

    // Sobrecarga de operadores para comparar dos conjuntos.
    public static bool operator ==(Set a, Set b) => Equals(a, b);
    public static bool operator !=(Set a, Set b) => !(a == b);
}