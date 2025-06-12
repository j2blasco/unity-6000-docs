* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.html

# UQueryBuilder<T0>
struct in UnityEngine.UIElements
/
Implemented in:[UnityEngine.UIElementsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.UIElementsModule.html)
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
Utility Object that constructs a set of selection rules to be run on a root visual element. 
A generic class that allows you to build queries for UI elements of type T. You can refine queries using selectors like name, class, and other conditions. It enables you to search for elements and execute the query on any VisualElement, making it easier to navigate and filter the VisualElement tree in large UIs, by type, name, class, and hierarchy conditions.  
  
For more information, refer to the [UQuery manual page](https://docs.unity3d.com/6000.0/Documentation/Manual/UIE-UQuery.html).   
  
The following example demonstrates how to use UQueryBuilder to find certain elements in a UI hierarchy and iterate over them: 
```
using UnityEngine;
using UnityEngine.UIElements;  
  
public class UQueryBuilderExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public UIDocument[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UIDocument.html) uiDocument;  
  
    private void OnEnable()
    {
        // Get the root visual element
        var root = uiDocument.rootVisualElement;  
  
        // Example query: Find all buttons with a specific class name
        var buttonQuery = new UQueryBuilder<Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html)>(root)
            .Class("my-button-class")
            .Build();  
  
        // Iterate over those buttons and add click handlers
        buttonQuery.ForEach(button => button.clicked += () => OnButtonClick(button));  
  
        // Another query: Find all labels that are descendants of elements with the class "container"
        var labelQuery = new UQueryBuilder<Label[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html)>(root)
            .Descendents<VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html)>("container")
            .Build();  
  
        // Change the text color of each label found
        labelQuery.ForEach(label => label.style.color = Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html));
    }  
  
    private void OnButtonClick(Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) button)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) with name {button.name} clicked.");
    }
}

```

### Constructors
Constructor | Description  
---|---  
[UQueryBuilder_1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1-ctor.html) |  Initializes a QueryBuilder.   
### Public Methods
Method | Description  
---|---  
[Active](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.Active.html) |  Selects all elements that are active.   
[AtIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.AtIndex.html) |  Convenience overload, shorthand for Build().AtIndex().   
[Build](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.Build.html) |  Compiles the selection rules into a QueryState object.   
[Checked](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.Checked.html) |  Selects all elements that are checked.   
[Children](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.Children.html) |  Selects all direct child elements of elements matching the previous rules.   
[Class](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.Class.html) |  Selects all elements with the specified class in the class list, as specified with the class attribute in a UXML file or added with VisualElement.AddToClassList method.   
[Descendents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.Descendents.html) |  Selects all elements that are descendants of currently matching ancestors.   
[Enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.Enabled.html) |  Selects all elements that are enabled.   
[First](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.First.html) |  Convenience overload, shorthand for Build().First().   
[Focused](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.Focused.html) |  Selects all elements that are focused.   
[ForEach](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.ForEach.html) |  Convenience overload, shorthand for Build().ForEach().   
[Hovered](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.Hovered.html) |  Selects all elements that are hovered.   
[Last](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.Last.html) |  Convenience overload, shorthand for Build().Last().   
[Name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.Name.html) |  Selects element with this name.   
[NotActive](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.NotActive.html) |  Selects all elements that are not active.   
[NotChecked](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.NotChecked.html) |  Selects all elements that not checked.   
[NotEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.NotEnabled.html) |  Selects all elements that are not enabled.   
[NotFocused](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.NotFocused.html) |  Selects all elements that don't currently own the focus.   
[NotHovered](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.NotHovered.html) |  Selects all elements that are not hovered.   
[NotVisible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.NotVisible.html) |  Selects all elements that are not visible.   
[OfType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.OfType.html) |  Selects all elements of the specified Type (eg: Label, Button, ScrollView, etc).   
[ToList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.ToList.html) |  Convenience method. shorthand for Build().ToList.   
[Visible](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.Visible.html) |  Selects all elements that are visible.   
[Where](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.UQueryBuilder_1.Where.html) |  Selects all elements satifying the predicate.   
* * *
