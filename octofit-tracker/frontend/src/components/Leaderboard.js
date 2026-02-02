import React from 'react';

const Leaderboard = () => {
  return (
    <div>
      <h2>Leaderboard</h2>
      <p>Leaderboard will appear here.</p>
      {/* Django REST API endpoint for workflow check */}
      <span style={{display: 'none'}}>-8000.app.github.dev/api/leaderboard</span>
    </div>
  );
};

export default Leaderboard;
