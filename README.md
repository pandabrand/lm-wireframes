# Las Mujeres wireframes

Low-fi wireframes for the 11 user stories in `Stuff for Fred/Other Stuff/User Stories.docx`, styled like the Paper Wireframe Kit (Patrick Hand, 2px black strokes, kit button and field shapes).

- `index.html`: every screen, grouped by user story. Open it in a browser to click through.
- `screens/*.html`: 24 standalone, responsive screens. Each has a green user-story note at the top that you can delete after import.
- `build.py`: generates the screens. Edit the copy or layout there, then run `python3 build.py`.

## Import into Figma (html.to.design)

1. Install the html.to.design plugin and its Chrome extension.
2. Open a screen in Chrome, for example `screens/01-home.html`.
3. Use the extension to send the page to Figma, choosing the Desktop (1440) and Mobile (375) viewports.
4. Alternative: in the plugin choose "Code" and paste the contents of a screen's HTML file. Fonts and styles are inline, so this works the same way.

Patrick Hand ships with Figma, so text keeps the kit's look after import.

## Screens by story

| Story | Screens |
|---|---|
| Overview | 01 Home |
| Farm | 02 About the Farm |
| Visual tour | 03 Visual Farm Tour |
| Products | 04 Wines & Ciders, 05 Product Detail |
| Label artists | 06 Artists, 07 Artist Detail |
| Farmers | 08 Growers, 09 Grower Detail |
| Tour or tasting | 10 Visit, 11 Request a Visit (email form), 12 Request Sent |
| Cabin + promo codes | 13 Cabin, 14 Dates & Promo (applied, invalid, special-guest and members-only states), 15 Details & Payment, 16 Confirmation |
| Club (B2C) | 17 Club, 18 Application form, 19 Application Sent |
| Trade availability (B2B) | 20 Trade Login, 21 Availability table, 22 Trade Enquiry (contact form) |
| Stockists | 23 Stockists (simple list by area, no search or map) |
| Newsletter | Footer form on every screen, 24 popup + error, already-subscribed and success states |

## Decisions (from the client)

- Tours and tastings: requests by email, no booking platform. The form emails the LM team, who confirm by reply.
- Cabin: bookings through Hapio.
- Club: run by hand by the client with spreadsheets. The site has an application form only: no member accounts, no online payment.
- No bottles sold online. Product pages point to stockists, the tasting room and the club.
- Tours are paid by Stripe invoice, sent by the LM team after they confirm. No payment on the site forms.

## Open questions for the client

- Club: how will members pay? Not decided yet. The wireframes say the team "arranges payment" so they work either way.
- Cabin: Hapio handles scheduling, not payments, so which payment provider? Do promo codes live in Hapio, or need custom logic? How are codes issued (per guest, shared, members only)?
- Club: membership tiers, prices, shipping states, and whether members get a cabin discount code.
- Trade availability: behind a login, or a public list without prices? Who updates the stock numbers, and how?
