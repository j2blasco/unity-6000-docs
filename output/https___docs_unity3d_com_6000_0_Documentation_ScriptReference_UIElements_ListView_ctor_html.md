* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ListView-ctor.html

# ListView Constructor
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
public ListView(); 
### Description
Creates a [ListView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ListView.html) with all default properties. The ListView.itemsSource must all be set for the ListView to function properly. 
* * *
## Declaration
public ListView(IList itemsSource, float itemHeight, Func<VisualElement> makeItem, Action<VisualElement,int> bindItem); 
### Parameters
Parameter | Description  
---|---  
itemsSource | The list of items to use as a data source.  
itemHeight | The height of each item, in pixels.  
makeItem | The factory method to call to create a display item. The method should return a VisualElement that can be bound to a data item.  
bindItem | The method to call to bind a data item to a display item. The method receives as parameters the display item to bind, and the index of the data item to bind it to.  
### Description
Constructs a [ListView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ListView.html), with all important properties provided. 
* * *
