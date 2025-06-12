* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-intValue.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).intValue
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
intValue; 
### Description
Value of an integer property.
Contains a valid value when [propertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-propertyType.html) is [SerializedPropertyType.Integer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.Integer.html) and the underlying type is signed 32 bit or smaller (e.g. sbyte, short and int). It is also appropriate for small unsigned types (ushort and byte). For 32 bit unsigned fields use [uintValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-uintValue.html) instead. And if you are accessing 64 bit integers use [longValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-longValue.html) or [ulongValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-ulongValue.html) instead.   
  
When assigning a value to [intValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-intValue.html), the value is clamped in the range of the property's declared type. For example, a property that is declared as a byte is clamped between 0 and 255.  
  
Additional resources: [intValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-intValue.html), [uintValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-uintValue.html), [longValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-longValue.html), [propertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-propertyType.html), [SerializedPropertyType.Integer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.Integer.html).
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Text;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class IntegerTypeExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public sbyte m_sbyte = SByte.MinValue;
    public byte m_byte = Byte.MaxValue;
    public short m_short = Int16.MinValue;
    public ushort m_ushort = UInt16.MaxValue;
    public int m_int = Int32.MinValue;
    public uint m_uint = UInt32.MaxValue;
    public long m_long = Int64.MinValue;
    public ulong m_ulong  = UInt64.MaxValue;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) Integer Access APIs")]
    static void TestMethod()
    {
        // This example demonstrates how to access the full range of each C# integer type via SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html)  
  
        IntegerTypeExample obj = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<IntegerTypeExample>();
        SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) sObj = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(obj);  
  
        var sb = new StringBuilder();
        sb.AppendLine($"m_sbyte  : {sObj.FindProperty("m_sbyte").intValue}");
        sb.AppendLine($"m_byte   : {sObj.FindProperty("m_byte").uintValue}"); // or intValue
        sb.AppendLine($"m_short  : {sObj.FindProperty("m_short").intValue}");
        sb.AppendLine($"m_ushort : {sObj.FindProperty("m_ushort").uintValue}"); // or intValue
        sb.AppendLine($"m_int    : {sObj.FindProperty("m_int").intValue}");
        sb.AppendLine($"m_uint   : {sObj.FindProperty("m_uint").uintValue}");
        sb.AppendLine($"m_long   : {sObj.FindProperty("m_long").longValue}");
        sb.AppendLine($"m_ulong  : {sObj.FindProperty("m_ulong").ulongValue}");  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(sb.ToString());
    }
}

```

* * *
