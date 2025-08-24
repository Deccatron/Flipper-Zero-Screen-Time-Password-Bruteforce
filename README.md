# Flipper-Zero-Screen-Time-Password-Bruteforce

A simple educational script that sequentially tests all possible 4 digit combinations to obtain the correct Screen Time passcode

---

**What does this do?**

This repository provides a simple wordlist and script which, when used with a Flipper Zero connected to an iPhone, exploits a vulnerability to bypass rate limiting. It then brute-forces every possible Screen Time PIN combination until successful, allowing the user to automatically retrieve the Screen Time passcode. With this method, the process can be completed in approximately 2 hours and 10 minutes with a 100% success rate, regardless of the iOS version.

---

**Instructions**

To start open the QFlipper app.

After that go to files and find the BadKB file.

Then go ahead and drag and drop the Screentime_Bypass.txt file into the BadKB file.

After thats done on your iphone go to settings.

Scroll to the bottom and click on "Transfer or Reset iPhone".

Click on "Erase All Content and Settings".

Press Continue.

Enter the password used to unlock the iphone.

Then it will ask for the Screen Time Passcode however there’s an interesting quirk the system doesn’t lock you out even after many incorrect attempts on the erasal menu.

Now plug in your Flipper Zero into the iphone preferably via USB-C

Head to BadKB and click on Screentime_Bypass

Click on configure and set BadKB to run off a USB connection instead of bluetooth (This may work with bluetooth but i havent tested).

Once configured head back to the Screentime_Bypass BadKB option and click run.

Allow the entire script to run until the correct password is found should take around 2 hours and 5 minutes minutes exactly (If using my stock configuration of 750 MS between each attempt which i reccomend since if its too fast the BadKB will input passwords faster than the phone can register meaning this wont work...)

Once the password has been found, click on the Cancel button to cancel the erasal.

Unfortunately there is no way to find out whether the correct password has been entered or not automatically. But instead just keep an eye on your iphone, once the script has found the correct password check the logs on the flipper's progress for running the script to see around which line was correct.

Open up the Screentime_Bypass.txt script using any text editor i prefer Visual Studio Code, and head to around which line number was the correct password.

Head back to "Transfer or Reset iPhone" on settings and head back to where it asks for the screen time password.

Go ahead and enter every combination from AROUND where the password was found until it unlocks.

Note that password down, and immediately cancel the erasal again.

And thats all! Screen Time Password cracked!

---

NOTE: I just had this idea while i was lying in bed, tried it and it worked perfectly. This is not meant for malicious usage but instead for educational purposes.

---
