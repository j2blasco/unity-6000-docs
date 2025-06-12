* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.SetParams.html

#  [Display](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html).SetParams
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
public void SetParams(int width, int height, int x, int y); 
### Parameters
Parameter | Description  
---|---  
width | Windows platforms only. The width of the window.  
height | Windows platforms only. The height of the window.  
x | Windows platforms only. The x position of the window.  
y | Windows platforms only. The y position of the window.  
### Description
Windows platforms only. Sets rendering size and position on screen.
To change the size and position of primary display you must also activate it by calling `Display.displays[0].Activate(0, 0, 0)`.
* * *
