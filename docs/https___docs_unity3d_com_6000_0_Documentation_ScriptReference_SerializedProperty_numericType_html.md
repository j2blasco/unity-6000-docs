* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-numericType.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).numericType
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
[SerializedPropertyNumericType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyNumericType.html) numericType; 
### Description
Return the precise type for Integer and Floating point properties. (Read Only)
The [propertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-propertyType.html) property classifies all supported Integer types as [SerializedPropertyType.Integer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.Integer.html), and both single and double precision Float types as [SerializedPropertyType.Float](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.Float.html). This property exposes the precise type, for example [SerializedPropertyNumericType.UInt8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyNumericType.UInt8.html) and [SerializedPropertyNumericType.Double](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyNumericType.Double.html), and is more efficient than using the string-based [type](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-type.html) property. For enum properties ([SerializedPropertyType.Enum](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.Enum.html)) it returns the underlying type. For non-numeric types it returns [SerializedPropertyNumericType.Unknown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyNumericType.Unknown.html). 
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Text;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class NumericTypeExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public byte m_byte;
    public int m_int;
    public long m_long;
    public float m_float;
    public double m_double;  
  
    [Flags[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html)]
    public enum UIntFlags : uint
    {
        None = 0,
        Flag31 = 1 << 30,
        Flag32 = 1u << 31,
    }
    public UIntFlags m_uintFlags;
    public string m_string;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) NumericType API")]
    static void TestMethod()
    {
        // This example demonstrates how numericType exposes more precise details of the type
        NumericTypeExample obj = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<NumericTypeExample>();
        SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(obj);  
  
        var serializedProperty = serializedObject.FindProperty("m_byte");
        var sb = new StringBuilder();
        do
        {
            sb.AppendLine(String.Format("Name: {0,-11} propertyType: {1,-7} numericType: {2}",
                serializedProperty.name, serializedProperty.propertyType, serializedProperty.numericType));
        }
        while (serializedProperty.Next(false));  
  
        //Expected output:
        //Name: m_byte      propertyType: Integer numericType: UInt8
        //Name: m_int       propertyType: Integer numericType: Int32
        //Name: m_long      propertyType: Integer numericType: Int64
        //Name: m_float     propertyType: Float   numericType: Float
        //Name: m_double    propertyType: Float   numericType: Double
        //Name: m_uintFlags propertyType: Enum    numericType: UInt32
        //Name: m_string    propertyType: String  numericType: Unknown
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(sb.ToString());
    }
}

```

* * *
