* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AddComponentMenu-ctor.html

# AddComponentMenu Constructor
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
public AddComponentMenu(string menuName); 
## Declaration
public AddComponentMenu(string menuName, int order); 
### Parameters
Parameter | Description  
---|---  
menuName | The path to the component.  
order | Where in the component menu to add the new item.  
### Description
Add an item in the Component menu.
The script will be placed in the component menu according to `menuName`. For example, if the `menuName` is "Rendering/DoSomething" the new menu will be called DoSomething and appear as a child of the `Rendering` group in the `Components` menu. If `menuName` is "" or starts with "/" the component will be hidden from the menu.   
Lower order values place the new item higher to the top of the Component menu.
* * *
