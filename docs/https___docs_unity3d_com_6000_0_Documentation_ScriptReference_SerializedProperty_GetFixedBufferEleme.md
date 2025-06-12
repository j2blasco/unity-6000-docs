* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.GetFixedBufferElementAtIndex.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).GetFixedBufferElementAtIndex
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
public [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) GetFixedBufferElementAtIndex(int index); 
### Description
Returns the element at the specified index in the fixed buffer.
Additional resources: [isFixedBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-isFixedBuffer.html), [fixedBufferSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-fixedBufferSize.html).
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
[System.Serializable]
public unsafe struct TestStruct
{
    public fixed int intBuffer[7];
}  
  
public unsafe class TestScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public TestStruct testStruct;  
  
    void Start()
    {
        fixed(int* buffer = testStruct.intBuffer)
        {
            for (int i = 0; i < 7; ++i)
                buffer[i] = 3 + i;
        }  
  
        var so = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(this);
        var prop = so.FindProperty("testStruct.intBuffer");  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("isFixedBuffer = " + prop.isFixedBuffer);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("fixedBufferSize = " + prop.fixedBufferSize);  
  
        var elemProp = prop.GetFixedBufferElementAtIndex(2);  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("GetFixedBufferElementAtIndex(2) = " + elemProp.intValue);  
  
        elemProp.intValue = 42;  
  
        so.ApplyModifiedProperties();  
  
        fixed(int* buffer = testStruct.intBuffer)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("intBuffer[2] = " + buffer[2]);
        }
    }
}

```

* * *
