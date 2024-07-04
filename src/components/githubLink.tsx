export const GitHubLink = () => {
  return (
    <div className="absolute right-0 z-10 m-24">
      <div className="p-8 rounded-16 bg-[#1F2328] flex">
        <img
          alt="Westpac Icon"
          height={24}
          width={24}
          src="/westpac-icon.png"  // Direct path to the image in the public folder
        ></img>
        <div className="mx-4 text-white font-M_PLUS_2 font-bold">Westpac</div>
      </div>
    </div>
  );
};
