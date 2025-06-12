* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAreaAttribute.html

# TextAreaAttribute
class in UnityEngine
/
Inherits from:[PropertyAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute.html)
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
### Description
Attribute to make a string be edited with a height-flexible and scrollable text area.
You can specify the minimum and maximum lines for the TextArea, and the field will expand according to the size of the text. A scrollbar will appear if the text is bigger than the area available.  
  
**Note:** The maximum lines refers to the maximum size of the TextArea. There is no maximum to the number of lines entered by the user.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/TextAreaAttribute.png)  
_Text Area in Inspector._
```
using UnityEngine;  
  
public class TextAreaExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    [TextAreaAttribute[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAreaAttribute.html)]
    public string MyTextArea;
}

```

### Properties
Property | Description  
---|---  
[maxLines](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAreaAttribute-maxLines.html) | The maximum amount of lines the text area can show before it starts using a scrollbar.  
[minLines](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAreaAttribute-minLines.html) | The minimum amount of lines the text area will use.  
### Constructors
Constructor | Description  
---|---  
[TextAreaAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAreaAttribute-ctor.html) | Attribute to make a string be edited with a height-flexible and scrollable text area.  
### Inherited Members
### Properties
Property | Description  
---|---  
[applyToCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute-applyToCollection.html) | Makes attribute affect collections instead of their items.  
[order](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute-order.html) | Optional field to specify the order that multiple DecorationDrawers should be drawn in.  
* * *
