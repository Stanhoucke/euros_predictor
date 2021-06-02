import React, { createContext } from 'react';

const PlayerContext = createContext({});
PlayerContext.displayName = "PlayerContext";

export const PlayerProvider = PlayerContext.Provider
export default PlayerContext