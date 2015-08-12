[![Build Status](https://travis-ci.org/Magana/ShippingTime.svg?branch=master)](https://travis-ci.org/Magana/ShippingTime)

###### Shipping carriers tell you what day your package will arrive, but what if we could tell people what ~~minute~~ their package will arrive?

The goal of this platform is that it will basically run itself after setup. By collecting user inputed data on what time packages arrived at their doorstep, where they live, what shipping carrier was used, and other information, we can build a model to give an accurate predicition of exactly when their shipment should arrive.

I think the easiest way to collect data would be asking users for the carrier, the tracking number, and their address. With this, we can automatically monitor the carrier's site and find out the time the carrier marked the shipment as delivered. This only works well if the carrier updates the shipment status quicky, so there might be a better approach.

_I meant for the word, "minute", to be an exaggeration. That's obviously impossible. Finding a 60 minute range would be quite impressive and seems like a reasonable goal for the learning system to hit in a couple of years._

#### Please contribute!
