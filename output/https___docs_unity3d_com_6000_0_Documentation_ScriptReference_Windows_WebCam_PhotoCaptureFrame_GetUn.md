* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.PhotoCaptureFrame.GetUnsafePointerToBuffer.html

#  [PhotoCaptureFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.PhotoCaptureFrame.html).GetUnsafePointerToBuffer
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
public IntPtr GetUnsafePointerToBuffer(); 
### Returns
**IntPtr** A native COM pointer to the IMFMediaBuffer which contains the image data. 
### Description
Provides a COM pointer to the native IMFMediaBuffer that contains the image data.
This method provides very low level access to the native COM IMFMediaBuffer object. Therefore care and caution should be applied when using this method.   
Please note that each time this method is invoked, an added reference will be applied to the IMFMediaBuffer COM pointer.   
The caller is responsible for releasing each instance of the COM pointer.  
  
For more information about the WinRT IMFMediaBuffer object, please visit <https://msdn.microsoft.com/en-us/library/windows/desktop/ms696261(v=vs.85).aspx>
* * *
