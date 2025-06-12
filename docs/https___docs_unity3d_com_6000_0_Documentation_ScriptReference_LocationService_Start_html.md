* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LocationService.Start.html

#  [LocationService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LocationService.html).Start
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
public void Start(); 
## Declaration
public void Start(float desiredAccuracyInMeters); 
## Declaration
public void Start(float desiredAccuracyInMeters, float updateDistanceInMeters); 
### Parameters
Parameter | Description  
---|---  
desiredAccuracyInMeters | The service accuracy you want to use, in meters. This determines the accuracy of the device's last location coordinates. Higher values like 500 don't require the device to use its GPS chip and thus save battery power. Lower values like 5-10 provide the best accuracy but require the GPS chip and thus use more battery power. The default value is 10 meters.  
updateDistanceInMeters | The minimum distance, in meters, that the device must move laterally before Unity updates [Input.location](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-location.html). Higher values like 500 produce fewer updates and are less resource intensive to process. The default is 10 meters.  
### Description
Starts location service updates.
After you call this function, you can access the device's last location coordinates by checking [lastData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LocationService-lastData.html) in [Input.location](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-location.html).  
  
**Note** : The location service doesn't start to send location data immediately. Therefore, check the [current service status](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LocationService-status.html) in [Input.location](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-location.html).  
  
On Android, using this method in scripts automatically adds the `ACCESS_FINE_LOCATION` permission to the android manifest. If you use low accuracy values like 500 or higher, select **Low Accuracy Location** in [Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html) to add the `ACCESS_COARSE_LOCATION` permission instead.  
  
On WebGL, this method must be invoked as a response to a user gesture (such as a mouse click) within a coroutine. **Note:** Geolocation services are available only with an HTTPS connection, except during development when you might use http://localhost. The use of `desiredAccuracyInMeters` and `updateDistanceInMeters` isn't supported since the user device determines those two values.
```
using UnityEngine;
using System.Collections;  
  
public class TestLocationService : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    IEnumerator Start()
    {
        // Check if the user has location service enabled.
        if (!Input.location.isEnabledByUser)
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Location[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilePathAttribute.Location.html) not enabled on device or app does not have permission to access location");  
  
        // Starts the location service.
        
        float desiredAccuracyInMeters = 10f;
        float updateDistanceInMeters = 10f;  
  
        Input.location.Start(desiredAccuracyInMeters, updateDistanceInMeters);  
  
        // Waits until the location service initializes
        int maxWait = 20;
        while (Input.location.status == LocationServiceStatus.Initializing[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LocationServiceStatus.Initializing.html) && maxWait > 0)
        {
            yield return new WaitForSeconds[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WaitForSeconds.html)(1);
            maxWait--;
        }  
  
        // If the service didn't initialize in 20 seconds this cancels location service use.
        if (maxWait < 1)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Timed out");
            yield break;
        }  
  
        // If the connection failed this cancels location service use.
        if (Input.location.status == LocationServiceStatus.Failed[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LocationServiceStatus.Failed.html))
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Unable to determine device location");
            yield break;
        }
        else
        {
            // If the connection succeeded, this retrieves the device's current location and displays it in the Console window.
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Location[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FilePathAttribute.Location.html): " + Input.location.lastData.latitude + " " + Input.location.lastData.longitude + " " + Input.location.lastData.altitude + " " + Input.location.lastData.horizontalAccuracy + " " + Input.location.lastData.timestamp);
        }  
  
        // Stops the location service if there is no need to query location updates continuously.
        Input.location.Stop();
    }
}

```

* * *
