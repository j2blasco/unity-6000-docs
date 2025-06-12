* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-androidVulkanDenyFilterList.html

#  [PlayerSettings.Android](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android.html).androidVulkanDenyFilterList
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html "Go to PlayerSettings Component in the Manual")
androidVulkanDenyFilterList; 
### Description
Specifies a list of [AndroidDeviceFilterData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidDeviceFilterData.html) parameters to restrict Android devices from using Vulkan API when running Unity applications.
Each parameter value in each [AndroidDeviceFilterData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidDeviceFilterData.html) entry is processed using logical AND operation to determine if the device matches the specified filter. The device is restricted from using Vulkan if its [AndroidDeviceFilterData.vulkanApiVersionString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidDeviceFilterData-vulkanApiVersionString.html) and [AndroidDeviceFilterData.driverVersionString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidDeviceFilterData-driverVersionString.html) values are less than or equal to the specified filter values, and it meets the other specified filter values.  
  
If you enter the same values in the [PlayerSettings.Android.androidVulkanAllowFilterList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.Android-androidVulkanAllowFilterList.html) and `PlayerSettings.Android.androidVulkanDenyFilterList` lists, Unity ignores the filter.
* * *
