* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.ForceUpdateCanvases.html

#  [Canvas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.html).ForceUpdateCanvases
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
public static void ForceUpdateCanvases(); 
### Description
Force all canvases to update their content.
A canvas performs its layout and content generation calculations at the end of a frame, just before rendering, in order to ensure that it's based on all the latest changes that may have happened during that frame. This means that in the Start callback and the first Update callback, the layout and content under the canvas may not be up-to-date.  
  
Code that relies on up-to-date layout or content can call this method to ensure it before executing code that relies on it.
* * *
