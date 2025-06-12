* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device.RequestStoreReview.html

#  [Device](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device.html).RequestStoreReview
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
public static bool RequestStoreReview(); 
### Returns
**bool** Value indicating whether the underlying API is available or not. False indicates that the iOS version isn't recent enough or that the StoreKit framework is not linked with the app. 
### Description
Request App Store rating and review from the user.
Use this method to indicate when it makes sense within the user experience flow of your application to ask the user for a review. Don't use buttons or other controls to request feedback because the actual display of a rating request is rate-limited and the user can opt-out of receiving these prompts. Make sure the user has demonstrated an engagement with your application before asking for a review. This will display the default Apple prompt that cannot be modified.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using UnityEngine;
using UnityEngine.iOS;  
  
public class RequestStoreReviewExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    bool reviewRequested = false;  
  
    void Start()
    {
        // Note: It is advised to request AppStore review after the user interacts with your application somehow, so doing it in Start wouldn't be ideal in real scenario.
        RequestReview();
    }  
  
    void RequestReview()
    {
        if (reviewRequested == false)
        {
            bool popupShown = Device.RequestStoreReview[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/iOS.Device.RequestStoreReview.html)();
            if (popupShown)
            {
                // The review popup was presented to the user, set "reviewRequested" to "true" to reflect that
                // Note: there's no way to check if the user actually gave a review for the app or cancelled the popup.
                reviewRequested = true;
            }
            else
            {
                // The review popup wasn't presented. Log a message and reset "reviewRequested" so you can revisit this in the future.
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("iOS[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.iOS.html) version is too low or StoreKit framework was not linked.");
                reviewRequested = false;
            }
        }
    }
}

```

* * *
