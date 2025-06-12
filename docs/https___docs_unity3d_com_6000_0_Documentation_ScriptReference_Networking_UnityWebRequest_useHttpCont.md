* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest-useHttpContinue.html

#  [UnityWebRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Networking.UnityWebRequest.html).useHttpContinue
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
useHttpContinue; 
### Description
Determines whether this UnityWebRequest will include `Expect: 100-Continue` in its outgoing request headers. (Default: `true`).
If this property is set to `true`, then this UnityWebRequest will include an `Expect: 100-Continue` header in the initial outbound request. If set to `false`, an empty `Expect` header will be sent, which will suppress usage of the `100 Continue` response code.  
  
As detailed in [RFC 2616, Section 8](https://www.w3.org/Protocols/rfc2616/rfc2616-sec8.html), the `100 Continue` response code is intended to allow a remote server to decide whether or not it will accept a request based on a request's headers, prior to the client transmitting the full request body.  
  
This is useful in cases where the client need not transmit its full request to every server in a request/response chain, such as in a load-balanced application. For example, a client would present its request, with a `Expect: 100-Continue` header, to a load-balancing server. The load-balancing server would then respond with a redirect to a processing server. Next, the client would connect to the processing server and transmit the same request, again with a `Expect: 100-Continue` server. The processing server would then respond with a `100 Continue` HTTP status code, and the client would finally respond with the full body of its request.  
  
By using the `100 Continue` status code, the client only had to transmit the full body of its request to one server. If not using the `100 Continue` status code, the client must transmit the full body of its request to every server it communicates with, needlessly consuming bandwidth and processing time on both the client and any servers issuing redirects.  
  
In general, one should leave `100 Continue` enabled. Exceptions include requests which have a very small or no request body, or applications where the client knows the server will not issue a redirect.  
  
This property defaults to `true`.  
  
**Note:** On WebGL build targets, header negotiation is performed by the host browser. Therefore, this setting's value has no effect on WebGL builds.
* * *
