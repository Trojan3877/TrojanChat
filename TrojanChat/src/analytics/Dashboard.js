/**
 * Dashboard.js
 *
 * Module: Analytics Dashboard
 * Author: Corey Leath
 *
 * A React component that fetches usage metrics from your backend or directly
 * from Firebase/GA endpoint and renders charts with Chart.js.
 */

import React, { useEffect, useState } from 'react';
import { Line, Bar } from 'react-chartjs-2';
import Chart from 'chart.js/auto';

// Replace with your real API or data fetch logic
const fetchAnalytics = async () => {
  // Example: fetch from your own endpoint that proxies GA or Firebase data
  const res = await fetch('/api/analytics/usage');
  return res.json();
};

export default function Dashboard() {
  const [metrics, setMetrics] = useState(null);

  useEffect(() => {
    fetchAnalytics().then(data => {
      setMetrics(data);
    });
  }, []);

  if (!metrics) {
    return <p>Loading analytics…</p>;
  }

  // Prepare Chart.js data structures
  const timeLabels = metrics.timestamps; // e.g. ["10:00", "11:00", ...]
  const usersData = {
    labels: timeLabels,
    datasets: [
      {
        label: 'Active Users',
        data: metrics.activeUsers,
        borderColor: 'rgba(75,192,192,1)',
        fill: false,
      },
    ],
  };

  const eventsData = {
    labels: timeLabels,
    datasets: [
      {
        label: 'Messages Sent',
        data: metrics.messagesSent,
        backgroundColor: 'rgba(153,102,255,0.6)',
      },
    ],
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h2>TrojanChat Usage Dashboard</h2>

      <section>
        <h3>Active Users Over Time</h3>
        <Line data={usersData} />
      </section>

      <section>
        <h3>Messages Sent Over Time</h3>
        <Bar data={eventsData} />
      </section>
    </div>
  );
}

git add TrojanChat/src/analytics/Dashboard.js
git commit -m "Add Analytics Dashboard component with Chart.js"
git push
