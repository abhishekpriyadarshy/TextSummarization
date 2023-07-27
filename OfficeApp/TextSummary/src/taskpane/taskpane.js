/*
 * Copyright (c) Microsoft Corporation. All rights reserved. Licensed under the MIT license.
 * See LICENSE in the project root for license information.
 */

/* global document, Office */

// Office.onReady((info) => {
//   if (info.host === Office.HostType.Outlook) {
//     document.getElementById("sideload-msg").style.display = "none";
//     document.getElementById("app-body").style.display = "flex";
//     document.getElementById("run").onclick = run;
//   }
// });

export async function run() {
  /**
   * Insert your Outlook code here
   */
}

Office.onReady(function (info) {
  // Assign a click event to a button with the id "processEmailButton"
  document.getElementById("processEmailButton").onclick = processEmail;
});

async function processEmail() {
  try {
    // Get the current item (email) from the Office context
    const item = Office.context.mailbox.item;

    // Read the email body
    await item.body.getAsync("text", function (result) {
      if (result.status === Office.AsyncResultStatus.Succeeded) {
        const emailBody = result.value;

        // Call the API to process the email body
        callApi(emailBody);
      } else {
        console.error("Error reading email body:", result.error);
      }
    });
  } catch (error) {
    console.error("Error processing email:", error);
  }
}

function callApi(data) {
  // Replace "API_URL" with your API endpoint URL
  const apiUrl = "API_URL";

  // Make a POST request to the API
  fetch(apiUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      data: data,
    }),
  })
    .then((response) => response.json())
    .then((result) => {
      console.log("API response:", result);
      // Handle the API response as needed
    })
    .catch((error) => console.error("API Error:", error));
}

