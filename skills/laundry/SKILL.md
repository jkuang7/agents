---
name: laundry
description: Book a one-time standard laundry pickup and return on laundromatpickup.com in the user's local Zen browser with Codex computer use. It picks the earliest pickup and return dates that are not same-day and whose noon–4 pm windows are clear on Google Calendar, and it leaves no tip. Use when the user runs /laundry, asks to book or schedule laundry pickup ("closest day possible"), or asks for a walkthrough of the booking flow.
---

# Laundry booking

## Runtime
- Required: Codex on GPT-6.1-Sol at high reasoning effort, driving the user's local, signed-in Zen browser with computer use (`cua_repl`).
- A skill cannot set the model, the effort level or the browser. If the session differs from this requirement or you can't tell, pause browser work, report accurately what is running or that it is unknown, and ask the user to choose an appropriate session. Never claim the runtime changed and never invent a setting.
- If computer use in Zen is unavailable, say so and stop. Never fall back to another browser or the site's booking APIs.
- You may use calendar connectors, but only to read availability. Never edit any calendar.

## Mode
- **Booking run:** the user asks to book or schedule. "Closest day possible" means the date rules below.
- **Walkthrough-only run:** the user asks to set up, test, show or verify the flow. Go as far as Review Order, report what you saw and stop. Never click the final button.

## Fixed choices
- Choose Standard delivery and One time. Never choose same-day pickup or same-day return because they cost more.
- Add no extras. Don't change the promo.
- Keep the saved address, payment method and laundry preferences. If any of them looks missing or different from the saved account, stop and ask the user.
- Tip: explicitly select NO TIP; leave 10/15/20/CUSTOM off and "Save tip for future orders" unchecked. Don't save any account-wide changes.

## Choosing dates
1. Use America/New_York as the service timezone. If the site UI shows a timezone, confirm that it matches.
2. List the calendars on every run.
   - Include personal and shared calendars that hold real commitments, including busy all-day events.
   - Exclude informational calendars such as holidays.
   - Read every page of results.
   - If a relevant calendar fails to load, report it and ask. Never assume that time is free.
3. Pickup date: the earliest date after today that the site offers and whose whole 12–4 pm window has no commitments.
4. Return date: the earliest date strictly after the pickup date that the site offers and whose whole 12–4 pm window is clear.
5. If 12–4 pm is blocked, move to a later date. Use a different time window only if the user allows it for this run.

## Site flow
Check every step against a fresh observation. Don't hardcode accessibility indices. Dialogs load asynchronously, so if a control is missing, observe again.
1. Open https://laundromatpickup.com/. If you aren't signed in, stop and ask the user to sign in.
2. Before starting a new order, check the account's existing open orders. If one already covers this request, report it and don't book a duplicate. Never cancel or edit a pre-existing order unless the user asks.
3. Click Schedule A Pickup. This leads to the curbsidelaundries order flow at `/app/order/DeliveryType`. Choose Standard delivery, then click Next.
4. On `/app/order/DeliveryDay`, choose One time. The page shows a default pickup and return; ignore these defaults. Pickup and return each have an unlabeled pencil button.
   - Pickup pencil: "Select pick up day" (dates shown as day/month), then Next, then "Select pick up time", choose 12–4, then Done.
   - Changing the pickup clears the return date and time, so set the return only after the pickup is set.
   - Return pencil: "Select delivery day" (offers only dates after the pickup), then Next, then "Select delivery time", choose 12–4, then Done.
   - Read the page again and confirm One time and that both dates and windows are exactly what you chose. Then click Next.
5. On `/app/order/ReviewOrder`, check that the address, payment method and laundry preferences match the saved account, that pickup and drop-off show the dates and windows you set (these intentionally differ from the defaults), and that the tip matches the fixed choices above.

## Final submit places the order
- The final button says "Continue to payment" and may briefly change to "Confirm order". Clicking it places the order using the saved card; no payment page follows. When the card is charged was not observed and cancellation was not investigated, so don't describe either. Treat this button as the submit button whatever its label says.
- The site shows no order total. The final price is set after the laundry is weighed. The delivery-type page shows the per-pound rate, and the homepage states the order minimum. Don't quote prices from memory.
- The runtime's computer-use policy decides whether you may submit. It requires an authorization that names the merchant (laundromatpickup.com), the purpose (this laundry order) and a spending limit.
  - If such an authorization for this order already exists under that policy and the order complies with it, submit without asking again.
  - Otherwise, at Review Order, show the user the dates and windows, the per-pound rate and the minimum as the site shows them. Explain that the total is variable and set after weighing. Ask for the merchant, purpose and spending-limit authorization the policy requires.
  - Approval of variable, weight-based pricing alone is not enough when the total can't be bounded to the authorized spending limit. If you can't establish that the total will stay within that limit, stop before submit and report, unless the runtime policy explicitly supports a user-approved variable-price transaction.
  - Never promise that the site enforces a cap or that the total will stay under it.
- Never submit during a walkthrough-only run.
- Click the final button once. If the result is unclear (a timeout, a spinner or a page error), never click it again. First look for `/app/order/Confirmation` or a new order in the account.

## Completion
- Confirm that `/app/order/Confirmation` shows "Your order is in!", then click Done. If the account lists orders, also check the dates, windows and zero tip there.
- Report the pickup date and window, the return date and window, the zero tip and any calendar caveats. Include no account details.
