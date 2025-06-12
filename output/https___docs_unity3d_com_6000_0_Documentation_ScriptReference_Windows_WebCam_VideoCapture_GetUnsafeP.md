* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.GetUnsafePointerToVideoDeviceController.html

#  [VideoCapture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Windows.WebCam.VideoCapture.html).GetUnsafePointerToVideoDeviceController
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
public IntPtr GetUnsafePointerToVideoDeviceController(); 
### Returns
**IntPtr** A native COM pointer to the IVideoDeviceController. 
### Description
Provides a COM pointer to the native IVideoDeviceController.
This method provides direct access to the native COM IVideoDeviceController object. Please use caution when calling this method. The IVideoDeviceController object allows you to control the device settings on the camera.   
Please note that a reference will be added to the IVideoDeviceController COM pointer each time this method is invoked.   
The caller is responsible for releasing each instance of the COM pointer.  
  
For more information, see Microsoft documentation on the [WinRT IVideoDeviceController object](https://docs.microsoft.com/en-us/uwp/api/Windows.Media.Devices.VideoDeviceController).
* * *
