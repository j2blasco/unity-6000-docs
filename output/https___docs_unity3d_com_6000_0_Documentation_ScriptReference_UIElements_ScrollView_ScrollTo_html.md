* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ScrollView.ScrollTo.html

#  [ScrollView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ScrollView.html).ScrollTo
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
public void ScrollTo([UIElements.VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) child); 
### Parameters
Parameter | Description  
---|---  
child | The child to scroll to.  
### Description
Scroll to a specific child element. 
This example creates a ScrollView that contains multiple labels. A Button is used to scroll to a selected label. 
```
using UnityEngine;
using UnityEngine.UIElements;  
  
public class ScrollViewScrollToExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public UIDocument[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UIDocument.html) uiDocument;
    public int numberOfLabels = 100;
    public int scrollToButton = 50;  
  
    Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)[] labels;  
  
    void Start()
    {
        var sv = new ScrollView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ScrollView.html) { name = "My Scroll View" };  
  
        labels = new Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)[numberOfLabels];
        for (int i = 0; i < numberOfLabels; i++)
        {
            var label = new Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html) { text = "Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) " + i };
            labels[i] = label;
            sv.Add(label);
        }  
  
        var button = new Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) { text = "Scroll to " + scrollToButton };
        button.clicked += DoScrollTo;  
  
        uiDocument.rootVisualElement.Add(button);
        uiDocument.rootVisualElement.Add(sv);
    }  
  
    void DoScrollTo()
    {
        var sv = uiDocument.rootVisualElement.Q<ScrollView[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ScrollView.html)>("My Scroll View");
        sv.ScrollTo(labels[scrollToButton]);
    }
}

```

* * *
