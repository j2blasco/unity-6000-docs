* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.Next.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).Next
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
## Declaration
public bool Next(bool enterChildren); 
### Description
Move to next property.
Update the SerializedProperty so that it points to the next property, in the order of serialization.  
  
This is can be used to traverse the state of objects without prior knowledge of their data structures. It is also an efficient way to iterate through arrays.  
  
If the current property is a compound type, such as an struct, array, string, or inline Unity struct such as [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html), then the enterChildren parameter determines whether to either visit the nested properties or to skip to the property immediately after the compound type.  
  
Next will never move to a different Object, so when the current property is of type [SerializedPropertyType.ObjectReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.ObjectReference.html) then calling Next(true) will not visit the properties of that referenced object. One way to visit a referenced object is to retrieve the object with [SerializedProperty.objectReferenceValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-objectReferenceValue.html) and construct a new SerializedObject instance for that target.  
  
If there are no further properties in the SerializedObject, this method will return false, and the SerializedProperty is set to an invalid state that not longer references a property. 
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using System.Text;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class SerializePropertyNextExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public long m_dataFirst = 45;
    public string m_data2 = "hi";  
  
    [Serializable]
    class NestedInline
    {
        public long[] m_data3 = new long[] {1, 2};
        public bool m_data4 = true;
    }
    [SerializeField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeField.html)]
    NestedInline m_nested;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) Next Example")]
    static void NextExample()
    {
        var scriptableObject = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<SerializePropertyNextExample>();  
  
        using (var serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(scriptableObject))
        {
            var sb = new StringBuilder();  
  
            // Visit the top level (depth 0) properties: m_dataFirst, m_data2 and m_nested
            VisitAll(serializedObject, false, sb);  
  
            // Visit each property, down to the granularity of individual string and array elements
            VisitAll(serializedObject, true, sb);
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(sb.ToString());
        }
    }  
  
    static void VisitAll(SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) serializedObject, bool visitChildren, StringBuilder report)
    {
        report.AppendLine($"Traversal result (visitChildren: {visitChildren})");  
  
        // Start at the first field, instead of using GetIterator(), in order to skip past the internal properties
        var serializedProperty = serializedObject.FindProperty("m_dataFirst");
        do
        {
            report.AppendLine($"\tFound {serializedProperty.propertyPath} (depth {serializedProperty.depth})");
        }
        while (serializedProperty.Next(visitChildren));
    }
}

```

```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Text;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class SerializePropertyArrayEnumerationWithNextExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    // Example of enumerating the elements of an array of struct using Next()
    [Serializable]
    public struct Data[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Data.html)
    {
        public int m_Data1;
        public string m_Data2;
    }  
  
    public Data[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Data.html)[] m_Data;
    public bool m_BeyondData;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) Array Enumeration Using Next")]
    static void TestArrayEnumeration()
    {
        var scriptableObject = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<SerializePropertyArrayEnumerationWithNextExample>();
        scriptableObject.m_Data = new Data[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Data.html)[]
        {
            new Data[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Data.html)() { m_Data1 = 0, m_Data2 = "zero" },
            new Data[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Data.html)() { m_Data1 = 1, m_Data2 = "one" },
            new Data[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Data.html)() { m_Data1 = 2, m_Data2 = "two" }
        };  
  
        var report = new StringBuilder();  
  
        using (var serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(scriptableObject))
        {
            var arrayProperty = serializedObject.FindProperty("m_Data");  
  
            var arrayElement = arrayProperty.GetArrayElementAtIndex(0);
            var arraySize = arrayProperty.arraySize;  
  
            for (int i = 0; i < arraySize; i++)
            {
                ReportElement(arrayElement, i, report);
                arrayElement.Next(false);
            }
        }
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(report.ToString());
    }  
  
    static void ReportElement(SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) arrayElement, int index, StringBuilder report)
    {
        var data1 = arrayElement.FindPropertyRelative("m_Data1").intValue;
        var data2 = arrayElement.FindPropertyRelative("m_Data2").stringValue;
        report.AppendLine($"Visiting Index {index}: {data1}, {data2}");
    }
}

```

If a SerializedProperty is referencing a ManagedReference, e.g. a field with the [SerializeReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html) attribute, and Next is called with enterChildren set to true, then the SerializedProperty will move to the first property inside the managed object. Because managed references can form cyclical graphs, calling Next(true) blindly could potentially cause an endless loop. The following example demonstrates a technique to avoid that.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using System.Text;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
[CreateAssetMenu]
public class SerializePropertyNextSerializeReferenceExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    [Serializable]
    public class Node[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Node.html)
    {
        public int m_Data;
        public string m_Data2;  
  
        [SerializeReference[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html)]
        public Node[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Node.html) m_Child1 = null;  
  
        [SerializeReference[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html)]
        public Node[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Node.html) m_Child2 = null;
    }  
  
    [SerializeReference[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html)]
    public Node[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Node.html) m_Front = null;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) Next Cyclic Graph Example")]
    static void TestNextOnCyclicGraph()
    {
        var scriptableObject = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<SerializePropertyNextSerializeReferenceExample>();  
  
        // Setup a graph of 3 nodes that has several cycles
        scriptableObject.m_Front = new Node[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Node.html)() { m_Data = 1, m_Data2 = "First Node[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Node.html)" };  
  
        var node2 = new Node[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Node.html)() { m_Data = 2, m_Data2 = "Second Node[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Node.html)", m_Child1 = scriptableObject.m_Front };
        scriptableObject.m_Front.m_Child1 = node2;  
  
        var node3 = new Node[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Node.html)() { m_Data = 3, m_Data2 = "Third Node[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Node.html)" };
        scriptableObject.m_Front.m_Child2 = node3;
        node2.m_Child2 = node3;
        node3.m_Child1 = scriptableObject.m_Front;  
  
        using (var serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(scriptableObject))
        {
            var serializedProperty = serializedObject.FindProperty("m_Front");  
  
            var sb = new StringBuilder();
            sb.AppendLine("Graph traversal result:");  
  
            // Track visited Node[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Node.html) objects by managed reference id to prevent endless looping
            var visitedNodes = new HashSet<long>();  
  
            bool visitChild;
            do
            {
                // default is false so we don't enumerate each character of each string,
                visitChild = false;  
  
                if (serializedProperty.propertyType == SerializedPropertyType.ManagedReference[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.ManagedReference.html))
                {
                    long refId = serializedProperty.managedReferenceId;
                    if (visitedNodes.Add(refId))
                        visitChild = true; // First time seeing node, so visit it
                }
                else if (serializedProperty.propertyType == SerializedPropertyType.String[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.String.html))
                {
                    sb.AppendLine($"Found {serializedProperty.propertyPath} : {serializedProperty.stringValue}");
                }
                else if (serializedProperty.propertyType == SerializedPropertyType.Integer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.Integer.html))
                {
                    sb.AppendLine($"Found {serializedProperty.propertyPath} : {serializedProperty.intValue}");
                }
            }
            while (serializedProperty.Next(visitChild));  
  
            /*Expected output
            Graph traversal result:
            Found m_Front.m_Data : 1
            Found m_Front.m_Data2 : First Node[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Node.html)
            Found m_Front.m_Child1.m_Data : 2
            Found m_Front.m_Child1.m_Data2 : Second Node[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Node.html)
            Found m_Front.m_Child1.m_Child2.m_Data : 3
            Found m_Front.m_Child1.m_Child2.m_Data2 : Third Node[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.Node.html)
            */
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(sb.ToString());
        }
    }
}

```

Additional resources: [NextVisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.NextVisible.html), [hasChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-hasChildren.html), [Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.Reset.html), [depth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-depth.html), [SerializedObject.GetIterator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.GetIterator.html), [GetEndProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.GetEndProperty.html).
* * *
