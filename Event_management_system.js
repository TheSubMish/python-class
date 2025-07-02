// MongoDB Event Management System 
// 0. DROP COLLECTIONS (CLEANUP)
db.participants.drop();
db.venues.drop();
db.events.drop();
db.eventBookings.drop();
db.bookingLog.drop();
db.sequences.drop();

// 1. CREATE COLLECTIONS WITH VALIDATION SCHEMAS
// Participants Collection
db.createCollection("participants", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["participant_id", "full_name", "contact_info", "address", "participant_type"],
      properties: {
        participant_id: { bsonType: "int" },
        full_name: { bsonType: "string", maxLength: 100 },
        contact_info: {
          bsonType: "object",
          required: ["phone", "email"],
          properties: {
            phone: { bsonType: "string", maxLength: 15 },
            email: { bsonType: "string", maxLength: 100 }
          }
        },
        address: {
          bsonType: "object",
          required: ["street", "city", "zip_code"],
          properties: {
            street: { bsonType: "string", maxLength: 100 },
            city: { bsonType: "string", maxLength: 50 },
            zip_code: { bsonType: "string", maxLength: 10 }
          }
        },
        participant_type: { enum: ["regular", "vip"] },
        vip_level: { bsonType: ["string", "null"], maxLength: 20 }
      }
    }
  }
});

// Venues Collection
db.createCollection("venues", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["venue_id", "name", "address"],
      properties: {
        venue_id: { bsonType: "int" },
        name: { bsonType: "string", maxLength: 100 },
        address: {
          bsonType: "object",
          required: ["street", "city", "zip_code"],
          properties: {
            street: { bsonType: "string", maxLength: 100 },
            city: { bsonType: "string", maxLength: 50 },
            zip_code: { bsonType: "string", maxLength: 10 }
          }
        },
        sponsors: {
          bsonType: "array",
          maxItems: 5,
          items: { bsonType: "string", maxLength: 100 }
        }
      }
    }
  }
});

// Events Collection
db.createCollection("events", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["event_id", "title", "event_date", "venue_id", "max_participants"],
      properties: {
        event_id: { bsonType: "int" },
        title: { bsonType: "string", maxLength: 200 },
        event_date: { bsonType: "date" },
        venue_id: { bsonType: "int" },
        max_participants: { bsonType: "int" },
        feedback: {
          bsonType: "array",
          items: {
            bsonType: "object",
            required: ["participant_id", "comment_text", "comment_date"],
            properties: {
              participant_id: { bsonType: "int" },
              comment_text: { bsonType: "string", maxLength: 300 },
              comment_date: { bsonType: "date" }
            }
          }
        }
      }
    }
  }
});

// EventBookings Collection
db.createCollection("eventBookings", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["booking_id", "participant_id", "event_id", "booking_date"],
      properties: {
        booking_id: { bsonType: "int" },
        participant_id: { bsonType: "int" },
        event_id: { bsonType: "int" },
        booking_date: { bsonType: "date" }
      }
    }
  }
});

// BookingLog Collection
db.createCollection("bookingLog", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["log_id", "participant_id", "event_id", "action", "log_date"],
      properties: {
        log_id: { bsonType: "int" },
        participant_id: { bsonType: "int" },
        event_id: { bsonType: "int" },
        action: { enum: ["BOOK", "CANCEL"] },
        log_date: { bsonType: "date" }
      }
    }
  }
});

// 2. CREATE INDEXES
// Participants indexes
db.participants.createIndex({ "participant_id": 1 }, { unique: true });
db.participants.createIndex({ "address.city": 1 });
db.participants.createIndex({ "participant_type": 1 });

// Venues indexes
db.venues.createIndex({ "venue_id": 1 }, { unique: true });
db.venues.createIndex({ "address.city": 1 });

// Events indexes
db.events.createIndex({ "event_id": 1 }, { unique: true });
db.events.createIndex({ "venue_id": 1 });
db.events.createIndex({ "event_date": 1 });

// EventBookings indexes
db.eventBookings.createIndex({ "booking_id": 1 }, { unique: true });
db.eventBookings.createIndex({ "participant_id": 1, "event_id": 1 }, { unique: true });
db.eventBookings.createIndex({ "event_id": 1 });
db.eventBookings.createIndex({ "booking_date": 1 });

// BookingLog indexes
db.bookingLog.createIndex({ "log_id": 1 }, { unique: true });
db.bookingLog.createIndex({ "participant_id": 1, "event_id": 1 });
db.bookingLog.createIndex({ "log_date": 1 });

// 3. INSERT SAMPLE DATA
// Insert Regular and VIP Participants
db.participants.insertMany([
  // Regular Participants
  {
    participant_id: 1,
    full_name: "Alice Johnson",
    contact_info: { phone: "9876543210", email: "alice@example.com" },
    address: { street: "123 Lane", city: "Kathmandu", zip_code: "44600" },
    participant_type: "regular",
    vip_level: null
  },
  {
    participant_id: 2,
    full_name: "Bob Thapa",
    contact_info: { phone: "9812345678", email: "bob@example.com" },
    address: { street: "456 Avenue", city: "Pokhara", zip_code: "33700" },
    participant_type: "regular",
    vip_level: null
  },
  {
    participant_id: 3,
    full_name: "Rita Lama",
    contact_info: { phone: "9801010101", email: "rita@example.com" },
    address: { street: "Sundhara", city: "Kathmandu", zip_code: "44600" },
    participant_type: "regular",
    vip_level: null
  },
  {
    participant_id: 4,
    full_name: "Sita Gurung",
    contact_info: { phone: "9802020202", email: "sita@example.com" },
    address: { street: "Chipledhunga", city: "Pokhara", zip_code: "33700" },
    participant_type: "regular",
    vip_level: null
  },
  {
    participant_id: 5,
    full_name: "Void Gaming",
    contact_info: { phone: "9811874212", email: "voidgaming@gmail.com" },
    address: { street: "Bharatpur-8", city: "Chitwan", zip_code: "44201" },
    participant_type: "regular",
    vip_level: null
  },
  {
    participant_id: 8,
    full_name: "John Doe",
    contact_info: { phone: "9876543210", email: "john@example.com" },
    address: { street: "789 Street", city: "Kathmandu", zip_code: "44600" },
    participant_type: "regular",
    vip_level: null
  },
  {
    participant_id: 9,
    full_name: "Jane Smith",
    contact_info: { phone: "9812345678", email: "jane@example.com" },
    address: { street: "321 Road", city: "Pokhara", zip_code: "33700" },
    participant_type: "regular",
    vip_level: null
  },
  // VIP Participants
  {
    participant_id: 6,
    full_name: "Diamond VIP",
    contact_info: { phone: "9800000000", email: "vip@example.com" },
    address: { street: "VIP Rd", city: "Lalitpur", zip_code: "44700" },
    participant_type: "vip",
    vip_level: "Gold"
  },
  {
    participant_id: 7,
    full_name: "Luffy",
    contact_info: { phone: "9812345678", email: "luffy@gmail.com" },
    address: { street: "East Blue", city: "One Piece_Japan", zip_code: "12312" },
    participant_type: "vip",
    vip_level: "Diamond"
  },
  {
    participant_id: 20,
    full_name: "Sarah Williams",
    contact_info: { phone: "9876543210", email: "sarah@vip.com" },
    address: { street: "123 VIP Boulevard", city: "Kathmandu", zip_code: "44600" },
    participant_type: "vip",
    vip_level: "Platinum"
  },
  {
    participant_id: 21,
    full_name: "Michael Johnson",
    contact_info: { phone: "9812345678", email: "michael@elite.com" },
    address: { street: "456 Elite Street", city: "Pokhara", zip_code: "33700" },
    participant_type: "vip",
    vip_level: "Diamond"
  },
  {
    participant_id: 22,
    full_name: "Emma Davis",
    contact_info: { phone: "9801234567", email: "emma@gold.com" },
    address: { street: "789 Gold Avenue", city: "Lalitpur", zip_code: "44700" },
    participant_type: "vip",
    vip_level: "Gold"
  }
]);

// Insert Venues
db.venues.insertMany([
  {
    venue_id: 1,
    name: "City Hall",
    address: { street: "Main Street", city: "Kathmandu", zip_code: "44600" },
    sponsors: ["Tech Corp", "Digital Solutions", "Innovation Hub", "Future Tech", "Smart Systems"]
  },
  {
    venue_id: 2,
    name: "Lakeside Arena",
    address: { street: "Lakeside Rd", city: "Pokhara", zip_code: "33700" },
    sponsors: ["Music World", "Sound Systems", "Event Masters", "Audio Pro", "Stage Craft"]
  },
  {
    venue_id: 3,
    name: "Heritage Center",
    address: { street: "Heritage Road", city: "Lalitpur", zip_code: "44700" },
    sponsors: ["Cultural Foundation", "Art Gallery", "Heritage Trust"]
  }
]);

// Insert Events with Feedback Data
db.events.insertMany([
  {
    event_id: 101,
    title: "Tech Conference 2025",
    event_date: ISODate("2025-09-10"),
    venue_id: 1,
    max_participants: 100,
    feedback: [
      {
        participant_id: 1,
        comment_text: "Great tech conference! Learned a lot about new technologies and networking opportunities.",
        comment_date: ISODate("2025-09-11T10:30:00Z")
      },
      {
        participant_id: 20,
        comment_text: "Excellent speakers and well organized event. The VIP experience was outstanding.",
        comment_date: ISODate("2025-09-12T14:15:00Z")
      },
      {
        participant_id: 3,
        comment_text: "Well organized event with valuable insights into emerging technologies.",
        comment_date: ISODate("2025-09-13T09:45:00Z")
      },
      {
        participant_id: 5,
        comment_text: "Amazing gaming session and tech demos. Would definitely attend again!",
        comment_date: ISODate("2025-09-14T16:20:00Z")
      }
    ]
  },
  {
    event_id: 102,
    title: "Music Festival",
    event_date: ISODate("2025-10-15"),
    venue_id: 2,
    max_participants: 200,
    feedback: [
      {
        participant_id: 2,
        comment_text: "Amazing music festival! Great lineup of artists and perfect sound quality.",
        comment_date: ISODate("2025-10-16T20:30:00Z")
      },
      {
        participant_id: 22,
        comment_text: "Perfect venue and atmosphere. The VIP area had excellent facilities.",
        comment_date: ISODate("2025-10-17T18:45:00Z")
      },
      {
        participant_id: 4,
        comment_text: "Loved the lakeside setting and the variety of music genres presented.",
        comment_date: ISODate("2025-10-18T12:15:00Z")
      }
    ]
  }
]);

// Insert Event Bookings
db.eventBookings.insertMany([
  { booking_id: 1, participant_id: 1, event_id: 101, booking_date: ISODate("2025-07-01T10:00:00Z") },
  { booking_id: 2, participant_id: 2, event_id: 102, booking_date: ISODate("2025-06-25T14:30:00Z") },
  { booking_id: 3, participant_id: 3, event_id: 101, booking_date: ISODate("2025-06-28T09:15:00Z") },
  { booking_id: 4, participant_id: 4, event_id: 102, booking_date: ISODate("2025-06-30T16:45:00Z") },
  { booking_id: 5, participant_id: 5, event_id: 101, booking_date: ISODate("2025-06-26T11:20:00Z") },
  { booking_id: 10, participant_id: 20, event_id: 101, booking_date: ISODate("2025-06-20T08:30:00Z") },
  { booking_id: 11, participant_id: 21, event_id: 101, booking_date: ISODate("2025-06-22T13:45:00Z") },
  { booking_id: 12, participant_id: 22, event_id: 102, booking_date: ISODate("2025-06-24T15:10:00Z") },
  { booking_id: 13, participant_id: 20, event_id: 102, booking_date: ISODate("2025-06-21T12:00:00Z") }
]);

// Insert Booking Log
db.bookingLog.insertMany([
  { log_id: 1, participant_id: 1, event_id: 101, action: "BOOK", log_date: ISODate("2025-07-01T10:00:00Z") },
  { log_id: 2, participant_id: 2, event_id: 102, action: "BOOK", log_date: ISODate("2025-06-25T14:30:00Z") },
  { log_id: 3, participant_id: 3, event_id: 101, action: "BOOK", log_date: ISODate("2025-06-28T09:15:00Z") },
  { log_id: 4, participant_id: 4, event_id: 102, action: "BOOK", log_date: ISODate("2025-06-30T16:45:00Z") },
  { log_id: 5, participant_id: 5, event_id: 101, action: "BOOK", log_date: ISODate("2025-06-26T11:20:00Z") },
  { log_id: 6, participant_id: 20, event_id: 101, action: "BOOK", log_date: ISODate("2025-06-20T08:30:00Z") },
  { log_id: 7, participant_id: 21, event_id: 101, action: "BOOK", log_date: ISODate("2025-06-22T13:45:00Z") },
  { log_id: 8, participant_id: 22, event_id: 102, action: "BOOK", log_date: ISODate("2025-06-24T15:10:00Z") },
  { log_id: 9, participant_id: 20, event_id: 102, action: "BOOK", log_date: ISODate("2025-06-21T12:00:00Z") }
]);



// QUERY A: Participant Event Bookings in Kathmandu 
db.eventBookings.aggregate([
  { $lookup: { from: "participants", localField: "participant_id", foreignField: "participant_id", as: "participant" }},
  { $lookup: { from: "events", localField: "event_id", foreignField: "event_id", as: "event" }},
  { $lookup: { from: "venues", localField: "event.venue_id", foreignField: "venue_id", as: "venue" }},
  { $unwind: "$participant" },
  { $unwind: "$event" },
  { $unwind: "$venue" },
  { $match: { "venue.address.city": "Kathmandu" }},
  {
    $project: {
      booking_id: 1,
      participant_id: "$participant.participant_id",
      full_name: "$participant.full_name",
      event_id: "$event.event_id",
      event_title: "$event.title",
      event_date: { $dateToString: { format: "%d-%m-%Y", date: "$event.event_date" }},
      venue_name: "$venue.name",
      venue_city: "$venue.address.city"
    }
  },
  { $sort: { booking_id: 1 }}
]);


// QUERY B: Event Feedback with Participant Type and Total Comments
db.events.aggregate([
  // 1️⃣  Add feedback count while it's still an array
  { $addFields: { total_feedback_count: { $size: "$feedback" } } },
  { $lookup: { from: "venues", localField: "venue_id", foreignField: "venue_id", as: "venue" } },
  { $unwind: "$venue" },
  { $unwind: "$feedback" },
  { $lookup: { from: "participants", localField: "feedback.participant_id", foreignField: "participant_id", as: "participant" } },
  { $unwind: "$participant" },
  {
    $addFields: {
      participant_status: {
        $cond: [
          { $eq: [ "$participant.participant_type", "vip" ] },
          { $concat: [ "VIP - ", "$participant.vip_level" ] },
          "Regular"
        ]
      }
    }
  },

  {
    $project: {
      event_id: 1,
      event_name: "$title",
      event_date: { $dateToString: { format: "%d-%m-%Y", date: "$event_date" } },
      venue_name: "$venue.name",
      participant_id: "$feedback.participant_id",
      comment_text: "$feedback.comment_text",
      feedback_date: { $dateToString: { format: "%d-%m-%Y %H:%M", date: "$feedback.comment_date" } },
      participant_name: "$participant.full_name",
      participant_email: "$participant.contact_info.email",
      participant_status: 1,
      total_feedback_count: 1      
    }
  },

  { $sort: { event_id: 1, "feedback.comment_date": -1 } }
]);




// QUERY C: Feedback and Sponsors per Event 
db.events.aggregate([
  { $lookup: { from: "venues", localField: "venue_id", foreignField: "venue_id", as: "venue" }},
  { $unwind: "$venue" },
  { $unwind: "$feedback" },
  { $lookup: { from: "participants", localField: "feedback.participant_id", foreignField: "participant_id", as: "participant" }},
  { $unwind: "$participant" },
  { $unwind: { path: "$venue.sponsors", preserveNullAndEmptyArrays: true }},
  {
    $project: {
      event_id: 1,
      event_title: "$title",
      participant_id: "$feedback.participant_id",
      full_name: "$participant.full_name",
      participant_status: {
        $cond: {
          if: { $eq: ["$participant.participant_type", "vip"] },
          then: { $concat: ["VIP - ", "$participant.vip_level"] },
          else: "Regular"
        }
      },
      comment_text: "$feedback.comment_text",
      feedback_date: { $dateToString: { format: "%d-%m-%Y", date: "$feedback.comment_date" }},
      sponsor: "$venue.sponsors"
    }
  },
  { $sort: { event_id: 1, "feedback.comment_date": 1 }}
]);
// QUERY D: Event Booking Time Analysis and VIP Trends 
db.events.aggregate([
  { $lookup: { from: "eventBookings", localField: "event_id", foreignField: "event_id", as: "bookings" }},
  { $unwind: "$bookings" },
  { $lookup: { from: "participants", localField: "bookings.participant_id", foreignField: "participant_id", as: "participant" }},
  { $unwind: "$participant" },
  {
    $addFields: {
      days_until_event: {
        $divide: [
          { $subtract: ["$event_date", new Date()] },
          1000 * 60 * 60 * 24
        ]
      },
      days_booked_in_advance: {
        $divide: [
          { $subtract: ["$event_date", "$bookings.booking_date"] },
          1000 * 60 * 60 * 24
        ]
      },
      booking_last_7_days: {
        $cond: {
          if: { $gte: ["$bookings.booking_date", { $subtract: [new Date(), 7 * 24 * 60 * 60 * 1000] }] },
          then: 1,
          else: 0
        }
      },
      booking_7_to_14_days: {
        $cond: {
          if: {
            $and: [
              { $gte: ["$bookings.booking_date", { $subtract: [new Date(), 14 * 24 * 60 * 60 * 1000] }] },
              { $lt: ["$bookings.booking_date", { $subtract: [new Date(), 7 * 24 * 60 * 60 * 1000] }] }
            ]
          },
          then: 1,
          else: 0
        }
      },
      is_vip: { $eq: ["$participant.participant_type", "vip"] }
    }
  },
  {
    $group: {
      _id: {
        event_id: "$event_id",
        title: "$title",
        event_date: "$event_date"
      },
      days_until_event: { $first: "$days_until_event" },
      first_booking_date: { $min: "$bookings.booking_date" },
      last_booking_date: { $max: "$bookings.booking_date" },
      bookings_last_7_days: { $sum: "$booking_last_7_days" },
      bookings_7_to_14_days_ago: { $sum: "$booking_7_to_14_days" },
      avg_days_booked_in_advance: { $avg: "$days_booked_in_advance" },
      vip_bookings: { $sum: { $cond: ["$is_vip", 1, 0] }},
      regular_bookings: { $sum: { $cond: ["$is_vip", 0, 1] }}
    }
  },
  {
    $addFields: {
      booking_period_days: {
        $divide: [
          { $subtract: ["$last_booking_date", "$first_booking_date"] },
          1000 * 60 * 60 * 24
        ]
      }
    }
  },
  {
    $project: {
      event_id: "$_id.event_id",
      event_name: "$_id.title",
      event_date: { $dateToString: { format: "%d-%m-%Y", date: "$_id.event_date" }},
      days_until_event: { $round: ["$days_until_event", 0] },
      first_booking_date: { $dateToString: { format: "%d-%m-%Y", date: "$first_booking_date" }},
      last_booking_date: { $dateToString: { format: "%d-%m-%Y", date: "$last_booking_date" }},
      booking_period_days: { $round: ["$booking_period_days", 0] },
      bookings_last_7_days: 1,
      bookings_7_to_14_days_ago: 1,
      avg_days_booked_in_advance: { $round: ["$avg_days_booked_in_advance", 1] },
      vip_bookings: 1,
      regular_bookings: 1,
      _id: 0
    }
  },
  { $sort: { days_until_event: 1 }}
]);



// QUERY E: Quarterly Participation Summary with Analytics =

db.events.aggregate([
  {
    $lookup: {
      from: "venues",
      localField: "venue_id",
      foreignField: "venue_id",
      as: "venue"
    }
  },
  {
    $lookup: {
      from: "eventBookings",
      localField: "event_id",
      foreignField: "event_id",
      as: "bookings"
    }
  },
  { $unwind: "$venue" },
  { $unwind: "$bookings" },
  {
    $lookup: {
      from: "participants",
      localField: "bookings.participant_id",
      foreignField: "participant_id",
      as: "participant"
    }
  },
  { $unwind: "$participant" },
  {
    $addFields: {
      quarter: {
        $concat: [
          { $toString: { $year: "$event_date" } },
          "-Q",
          { $toString: { $ceil: { $divide: [{ $month: "$event_date" }, 3] } } }
        ]
      },
      participant_type: {
        $cond: {
          if: { $eq: ["$participant.participant_type", "vip"] },
          then: "VIP",
          else: "Regular"
        }
      }
    }
  },
  {
    $group: {
      _id: {
        city: "$venue.address.city",
        quarter: "$quarter",
        participant_type: "$participant_type"
      },
      participant_count: { $addToSet: "$bookings.participant_id" },
      event_count: { $addToSet: "$event_id" }
    }
  },
  {
    $addFields: {
      participant_count: { $size: "$participant_count" },
      event_count: { $size: "$event_count" }
    }
  },
  {
    $group: {
      _id: {
        city: "$_id.city",
        quarter: "$_id.quarter"
      },
      details: {
        $push: {
          participant_type: "$_id.participant_type",
          participant_count: "$participant_count",
          event_count: "$event_count"
        }
      },
      total_participants: { $sum: "$participant_count" }
    }
  },
  {
    $project: {
      city: "$_id.city",
      quarter: "$_id.quarter",
      details: 1,
      total_participants: 1,
      _id: 0
    }
  },
  { $sort: { city: 1, quarter: 1 } }
]);