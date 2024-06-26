#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Return an empty object if w or h is not a positive integer or is equal to 0
      return {};
    }
  }
}

module.exports = Rectangle;
