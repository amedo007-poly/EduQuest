FROM node:18-alpine

WORKDIR /app

# Install dependencies
COPY package.json .
RUN npm install

# Copy app
COPY . .

# Expose port
EXPOSE 3000

# Run
CMD ["npm", "start"]
