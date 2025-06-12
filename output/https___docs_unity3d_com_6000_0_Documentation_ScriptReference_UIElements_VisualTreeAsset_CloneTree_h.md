* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualTreeAsset.CloneTree.html

#  [VisualTreeAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualTreeAsset.html).CloneTree
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
public [UIElements.TemplateContainer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TemplateContainer.html) CloneTree(); 
### Returns
**TemplateContainer** The root of the tree of VisualElements that was just cloned. 
### Description
Build a tree of VisualElements from the asset. 
* * *
## Declaration
public [UIElements.TemplateContainer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TemplateContainer.html) CloneTree(string bindingPath); 
### Parameters
Parameter | Description  
---|---  
bindingPath | The path to the property that you want to bind to the root of the cloned tree.  
### Returns
**TemplateContainer** The root of the tree of VisualElements that was just cloned. 
### Description
Build a tree of VisualElements from the asset. 
* * *
## Declaration
public void CloneTree([UIElements.VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) target); 
### Parameters
Parameter | Description  
---|---  
target | A VisualElement that will act as the root of the cloned tree.  
### Description
Builds a tree of VisualElements from the asset. 
* * *
