import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

const App = () => {
  const [userData, setUserData] = useState([]);

  const twitterUrls = [
    'https://twitter.com/GTNUK1',
    'https://twitter.com/whatsapp',
    'https://twitter.com/aacb_CBPTrade',
    'https://twitter.com/aacbdotcom',
    'https://twitter.com/@AAWindowPRODUCT',
    'https://www.twitter.com/aandb_kia',
    'https://twitter.com/ABHomeInc',
    'https://twitter.com/Abrepro',
    'https://twitter.com/ACChristofiLtd',
    'https://twitter.com/aeclothing1',
    'https://twitter.com/AETechnologies1',
    'http://www.twitter.com/wix',
    'https://twitter.com/AGInsuranceLLC'
  ];

  const handleFetch = async () => {
    try {
      const response = await axios.post('http://localhost:7000/scrape', {
        urls: twitterUrls
      });
      setUserData(response.data.user_data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div className="app-container">
      <h1 className="app-header">Twitter Scraper</h1>
      <button onClick={handleFetch} className="fetch-button">
        Fetch Data
      </button>
      <div className="profile-cards-container">
        {userData.map((user, index) => (
          <div key={index} className="profile-card">
            {user.profile_image_url && user.profile_image_url !== "Profile image not found" && (
              <img src={user.profile_image_url} alt="Profile" className="profile-image" />
            )}
            <div className="profile-info">
              <h2>{user.username}</h2>
              <p className="bio">{user.bio || 'N/A'}</p>
              <p><strong>Followers:</strong> {user.followers || 'N/A'}</p>
              <p><strong>Following:</strong> {user.following || 'N/A'}</p>
              <p><strong>Location:</strong> {user.location || 'N/A'}</p>
              <p><strong>Website:</strong> 
                <a href={user.website || '#'} target="_blank" rel="noopener noreferrer">
                  {user.website || 'N/A'}
                </a>
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default App;
